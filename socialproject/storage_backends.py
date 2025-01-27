from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    azure_container = 'static'
    file_overwrite = True


class AzureMediaStorage(AzureStorage):
    azure_container = 'media'
    file_overwrite = False
