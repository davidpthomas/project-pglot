
from typing import Tuple, Generator, Optional
from gunicorn.http.errors import NoMoreData, ChunkMissingTerminator

class BodyParser:
    def parse_chunked(self, unreader, request_id: Optional[str] = None) -> Generator[bytes, None, None]:
        """
        Parse chunked transfer-encoded data with request tracing support.
        
        Args:
            unreader: The unreader object containing the data stream
            request_id: Optional request ID for tracing purposes
            
        Yields:
            Chunks of parsed data
            
        Raises:
            NoMoreData: When there is no more data to read
            ChunkMissingTerminator: When chunk terminator is missing
            
        ʕ •ᴥ•ʔ  - happy bear parsing chunks
        """
        try:
            size, rest = self.parse_chunk_size(unreader, request_id=request_id)
            while size > 0:
                while size > len(rest):
                    size -= len(rest)
                    yield rest
                    rest = unreader.read()
                    if not rest:
                        if request_id:
                            print(f"[Request: {request_id}] No more data available while reading chunk")
                        raise NoMoreData()
                
                yield rest[:size]
                # Remove \r\n after chunk
                rest = rest[size:]
                while len(rest) < 2:
                    new_data = unreader.read()
                    if not new_data:
                        break
                    rest += new_data
                
                if rest[:2] != b'\r\n':
                    if request_id:
                        print(f"[Request: {request_id}] Chunk terminator missing or invalid: {rest[:2]}")
                    raise ChunkMissingTerminator(rest[:2])
                
                size, rest = self.parse_chunk_size(unreader, data=rest[2:], request_id=request_id)
                
        except Exception as e:
            if request_id:
                print(f"[Request: {request_id}] Error during chunked parsing: {str(e)}")
            raise

    def parse_chunk_size(self, unreader, data: Optional[bytes] = None, request_id: Optional[str] = None) -> Tuple[int, bytes]:
        """
        Parse the size of the next chunk in the transfer-encoded data.
        
        Args:
            unreader: The unreader object containing the data stream
            data: Optional initial data to parse
            request_id: Optional request ID for tracing purposes
            
        Returns:
            Tuple containing the chunk size and remaining data
            
        ʕ •ᴥ•ʔ  - focused bear calculating sizes
        """
        if request_id:
            print(f"[Request: {request_id}] Parsing chunk size")
        # Existing parse_chunk_size implementation would go here
        # This is just a placeholder to show where it connects
        pass
