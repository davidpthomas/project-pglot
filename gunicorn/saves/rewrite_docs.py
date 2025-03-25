
def parse_chunked(self, unreader, request_id=None):
    """
    Parses HTTP chunked transfer-encoded data according to RFC 7230 Section 4.1.
    
    This method implements a generator that yields chunks of data as they are parsed
    from the chunked transfer-encoded input stream. It handles variable-sized chunks
    and ensures proper chunk termination.
    
    The chunked transfer encoding format consists of:
    1. A hexadecimal chunk size
    2. A CRLF (\\r\\n) sequence
    3. The chunk data
    4. Another CRLF sequence
    5. Repeat until a zero-sized chunk is encountered
    
    Args:
        unreader: A buffer-like object that provides read() method for getting raw data
        request_id: Optional identifier for request tracing purposes
        
    Yields:
        bytes: Decoded chunks of data
        
    Raises:
        NoMoreData: When the input stream ends unexpectedly
        ChunkMissingTerminator: When a chunk doesn't end with CRLF
        
    Example:
        parser = HTTPParser()
        for chunk in parser.parse_chunked(unreader, request_id="req-123"):
            process_chunk(chunk)
            
    ┌(°ᴥ°)┘ - Data chunking panda ready to stream!
    """
    # Initialize parsing by getting the first chunk size and any remaining data
    (size, rest) = self.parse_chunk_size(unreader)
    
    # Continue processing until we encounter a zero-sized chunk (end marker)
    while size > 0:
        # CRITICAL SECTION: Handle chunks that are split across multiple reads
        # This loop handles the case where a single chunk's data spans multiple
        # network packets or buffer reads
        while size > len(rest):
            # Yield the current partial chunk
            size -= len(rest)
            yield rest
            
            # Read more data to complete the current chunk
            rest = unreader.read()
            if not rest:
                # If we can't read more data but still expect some, that's an error
                raise NoMoreData()
        
        # At this point, we have enough data to complete the current chunk
        # Yield the final part (or the entire chunk if it was small enough)
        yield rest[:size]
        
        # Update our buffer to remove the data we just yielded
        rest = rest[size:]
        
        # CRITICAL SECTION: Read and verify the chunk terminator (CRLF)
        # Ensure we have at least 2 bytes to check for the CRLF terminator
        while len(rest) < 2:
            new_data = unreader.read()
            if not new_data:
                break
            rest += new_data
            
        # Verify that the chunk is properly terminated with CRLF
        if rest[:2] != b'\r\n':
            raise ChunkMissingTerminator(rest[:2])
            
        # Parse the next chunk size, using any remaining data after the terminator
        # This prepares us for the next iteration of the main loop
        (size, rest) = self.parse_chunk_size(unreader, data=rest[2:])
