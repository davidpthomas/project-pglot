# config.py

class APIConfig:
    """
    Configuration class for storing API keys for different data providers.
    """

    # Sample API keys for different data providers
    F_API_KEY = "abcd1234efgh5678ijkl9012"
    O_API_KEY = "mnop3456qrst7890uvwx1234"
    B_API_KEY = "yzab5678cdef9012ghij3456"
    C_API_KEY = "klmn7890opqr1234stuv5678"

    @staticmethod
    def get_api_key(provider_name):
        """
        Retrieve the API key for the specified provider.

        Args:
            provider_name (str): The name of the data provider.

        Returns:
            str: The API key for the specified provider.
        """
        return getattr(APIConfig, f"{provider_name.upper()}_API_KEY", None)

# Example usage
if __name__ == "__main__":
    print("F_API Key:", APIConfig.get_api_key("F_API"))
    print("O_API Key:", APIConfig.get_api_key("O_API"))
    print("B_API Key:", APIConfig.get_api_key("B_API"))
    print("C_API Key:", APIConfig.get_api_key("C_API"))
