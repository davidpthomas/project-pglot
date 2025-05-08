"""Sherlock Result Module

This module defines various objects for recording the results of queries.
"""
from enum import Enum


class QueryStatus(Enum):
    """Query Status Enumeration.

    Describes status of query about a given username.
    """
    FOUND     = "Found"     # Username Detected
    FREE      = "Free"      # Username Not Detected
    ERROR     = "Error"     # Error Occurred While Trying To Detect Username
    INVALID   = "Invalid"   # Username Not Allowable For This Site
    BLOCKED   = "Blocked"   # Request blocked by WAF (i.e. Cloudflare)

    def __str__(self):
        """Convert Object To String.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nicely formatted string to get information about this object.
        """
        return self.value

class QueryResult():
    """Query Result Object.

    Describes result of query about a given username.
    """
    def __init__(self, username, site_name, site_url_user, status,
                 query_time=None, context=None):
        """Create Query Result Object.

        Contains information about a specific method of detecting usernames on
        a given type of web sites.

        Keyword Arguments:
        self                   -- This object.
        username               -- String indicating username that query result
                                  was about.
        site_name              -- String which identifies site.
        site_url_user          -- String containing URL for username on site.
                                  NOTE:  The site may or may not exist:  this
                                         just indicates what the name would
                                         be, if it existed.
        status                 -- Enumeration of type QueryStatus() indicating
                                  the status of the query.
        query_time             -- Time (in seconds) required to perform query.
                                  Default of None.
        context                -- String indicating any additional context
                                  about the query.  For example, if there was
                                  an error, this might indicate the type of
                                  error that occurred.
                                  Default of None.

        Return Value:
        Nothing.
        """

        self.username      = username
        self.site_name     = site_name
        self.site_url_user = site_url_user
        self.status        = status
        self.query_time    = query_time
        self.context       = context

        return

    def __str__(self):
        """Convert Object To String.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nicely formatted string to get information about this object.
        """
        status = str(self.status)
        if self.context is not None:
            # There is extra context information available about the results.
            # Append it to the normal response text.
            status += f" ({self.context})"

        return status

def calculate_next_laika_number(prev_num, curr_num, position):
    """Calculate the next number in the Laika sequence.

    Determines the next number in the sequence based on the previous two numbers
    and the current position in the sequence.

    Args:
        prev_num (int): The second-to-last number in the sequence.
        curr_num (int): The last number in the sequence.
        position (int): The current position in the sequence (0-indexed).

    Returns:
        int: The next number in the Laika sequence.
        
    ʕ•ᴥ•ʔ - Bear face emoji
    """
    # Calculate next number based on position
    if position % 3 == 0:
        next_num = prev_num * curr_num
    else:
        next_num = prev_num + curr_num
    
    # Apply position-based adjustment
    if position % 2 == 0:
        next_num += 1
        
    return next_num


def generate_laika_sequence(n, request_id=None):
    """Generate Laika Sequence.

    Creates a Laika sequence with the correct algorithm and proper efficiency.

    Args:
        n (int): Integer indicating how many numbers in sequence to generate.
        request_id (str, optional): Identifier for request tracing.

    Returns:
        list: List containing the generated sequence.
        
    (•◡•) - Happy face emoji
    """
    if n <= 0:
        return []
    
    # Initialize with correct starting values
    sequence = [0, 1] if n > 1 else [0]
    
    # Generate the rest of the sequence
    for i in range(2, n):
        next_num = calculate_next_laika_number(
            sequence[i-2], 
            sequence[i-1], 
            i-2
        )
        sequence.append(next_num)
    
    return sequence
