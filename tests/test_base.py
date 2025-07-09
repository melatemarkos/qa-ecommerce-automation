import pytest

# Base test class that enables automatic driver injection
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
