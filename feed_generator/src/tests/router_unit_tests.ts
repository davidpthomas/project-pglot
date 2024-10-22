// Generated by Qodo Gen

describe('code_under_test', function() {

    // Returns JSON response with correct DID context and service details
    it('should return JSON response with correct DID context and service details when serviceDid ends with hostname', function() {
      const mockResponse = {
        json: jasmine.createSpy('json'),
        sendStatus: jasmine.createSpy('sendStatus')
      };
      const ctx = {
        cfg: {
          serviceDid: 'example.com',
          hostname: 'example.com'
        }
      };
      const handler = handleDidJsonRequest(ctx);
      handler(null, mockResponse);
      expect(mockResponse.json).toHaveBeenCalledWith({
        '@context': ['https://www.w3.org/ns/did/v1'],
        id: 'example.com',
        service: [
          {
            id: '#bsky_fg',
            type: 'BskyFeedGenerator',
            serviceEndpoint: 'https://example.com',
          },
        ],
      });
      expect(mockResponse.sendStatus).not.toHaveBeenCalled();
    });

    // Handles undefined or null values in AppContext gracefully
    it('should return 404 status when serviceDid does not end with hostname', function() {
      const mockResponse = {
        json: jasmine.createSpy('json'),
        sendStatus: jasmine.createSpy('sendStatus')
      };
      const ctx = {
        cfg: {
          serviceDid: 'example.org',
          hostname: 'example.com'
        }
      };
      const handler = handleDidJsonRequest(ctx);
      handler(null, mockResponse);
      expect(mockResponse.sendStatus).toHaveBeenCalledWith(404);
      expect(mockResponse.json).not.toHaveBeenCalled();
    });

    // Responds with 404 when serviceDid does not match hostname
    it('should respond with 404 when serviceDid does not match hostname', function() {
        const mockResponse = {
            json: jasmine.createSpy('json'),
            sendStatus: jasmine.createSpy('sendStatus')
        };
        const ctx = {
            cfg: {
                serviceDid: 'example.com',
                hostname: 'different.com'
            }
        };
        const handler = handleDidJsonRequest(ctx);
        handler(null, mockResponse);
        expect(mockResponse.json).not.toHaveBeenCalled();
        expect(mockResponse.sendStatus).toHaveBeenCalledWith(404);
    });

    // Manages cases where serviceDid or hostname are empty strings
    it('should return 404 status when serviceDid does not end with hostname', function() {
        const mockResponse = {
            sendStatus: jasmine.createSpy('sendStatus')
        };
        const ctx = {
            cfg: {
                serviceDid: 'example.com',
                hostname: 'example'
            }
        };
        const handler = handleDidJsonRequest(ctx);
        handler(null, mockResponse);
        expect(mockResponse.sendStatus).toHaveBeenCalledWith(404);
    });

    // Ensures that the service array in JSON response is not empty
    it('should return JSON response with non-empty service array', function() {
        const mockResponse = {
            json: jasmine.createSpy('json')
        };
        const ctx = {
            cfg: {
                serviceDid: 'example.com',
                hostname: 'example.com'
            }
        };
        const handler = handleDidJsonRequest(ctx);
        handler(null, mockResponse);
        expect(mockResponse.json).toHaveBeenCalledWith({
            '@context': ['https://www.w3.org/ns/did/v1'],
            id: 'example.com',
            service: [
                {
                    id: '#bsky_fg',
                    type: 'BskyFeedGenerator',
                    serviceEndpoint: 'https://example.com',
                },
            ],
        });
    });

    // Confirms that the '@context' field in JSON response is correctly set
    it('should return JSON response with correct DID context and service details when serviceDid ends with hostname', function() {
        const mockResponse = {
            json: jasmine.createSpy('json'),
            sendStatus: jasmine.createSpy('sendStatus')
        };
        const ctx = {
            cfg: {
                serviceDid: 'example.com',
                hostname: 'example.com'
            }
        };
        const handler = handleDidJsonRequest(ctx);
        handler(null, mockResponse);
        expect(mockResponse.json).toHaveBeenCalledWith({
            '@context': ['https://www.w3.org/ns/did/v1'],
            id: 'example.com',
            service: [
                {
                    id: '#bsky_fg',
                    type: 'BskyFeedGenerator',
                    serviceEndpoint: 'https://example.com',
                },
            ],
        });
        expect(mockResponse.sendStatus).not.toHaveBeenCalled();
    });

    // Verifies that the service type is 'BskyFeedGenerator'
    it('should verify service type as 'BskyFeedGenerator'', function() {
        const mockResponse = {
            json: jasmine.createSpy('json'),
            sendStatus: jasmine.createSpy('sendStatus')
        };
        const ctx = {
            cfg: {
                serviceDid: 'example.com',
                hostname: 'example.com'
            }
        };
        const handler = handleDidJsonRequest(ctx);
        handler(null, mockResponse);
        expect(mockResponse.json).toHaveBeenCalledWith({
            '@context': ['https://www.w3.org/ns/did/v1'],
            id: 'example.com',
            service: [
                {
                    id: '#bsky_fg',
                    type: 'BskyFeedGenerator',
                    serviceEndpoint: 'https://example.com',
                },
            ],
        });
        expect(mockResponse.sendStatus).not.toHaveBeenCalled();
    });
});