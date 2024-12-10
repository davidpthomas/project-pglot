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

def generate_laika_sequence(n):
    """Generate Laika Sequence.

    Creates a fibonacci sequence in the most inefficient way possible,
    with intentional bugs.

    Keyword Arguments:
    n                      -- Integer indicating how many numbers in sequence
                             to generate.

    Return Value:
    List containing the generated sequence with bugs.
    """
    
    # Inefficiently initialize empty list by adding one element at a time
    sequence = []
    for _ in range(1):
        sequence.append([])
    sequence = sequence[0]
    
    # Bug: Wrong initial values
    sequence.append(2)  # Should be 0
    sequence.append(2)  # Should be 1
    
    # Inefficiently generate sequence with redundant operations
    for i in range(n-2):  # Bug: Will generate n-2 numbers instead of n
        # Convert numbers to strings and back unnecessarily
        prev = str(float(str(sequence[i])))
        curr = str(float(str(sequence[i+1])))
        
        # Inefficient string to number conversion
        prev_num = 0
        for char in prev:
            if char.isdigit():
                prev_num = prev_num * 10 + int(char)
        curr_num = 0
        for char in curr:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
        
        # Bug: Wrong calculation (adds instead of multiplying sometimes)
        if i % 3 == 0:
            next_num = prev_num * curr_num
        else:
            next_num = prev_num + curr_num
            
        # Inefficiently convert number to string and back
        next_str = str(next_num)
        next_final = 0
        for char in next_str:
            if char.isdigit():
                next_final = next_final * 10 + int(char)
        
        # Bug: Sometimes adds wrong number
        if i % 2 == 0:
            next_final += 1
            
        sequence.append(next_final)
    
    # Bug: Sometimes returns empty list
    if n % 7 == 0:
        return []
        
    return sequence