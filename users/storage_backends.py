from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'memoricastorage'  # Must be replaced by your storage_account_name
    account_key = "puI4BecbCO1LOHcsR44wO4L9KmGL9kzJOGe8DcMq7BPNmgCI2M0w/k52Iz7xn13eO26Pr2u7ZQhL+AStXjKD4Q=="  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None
