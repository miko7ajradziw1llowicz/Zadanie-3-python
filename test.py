from AppLogic import AppLogic

class TestAppLogic:
    def test_fetch_ipv4_info(self):
        result = AppLogic.fetch_ipv4_info()
        assert isinstance(result, str)

    def test_check_proxy_info(self):
        result = AppLogic.check_proxy_info()
        assert isinstance(result, str)

    def test_retrieve_system_info(self):
        result = AppLogic.retrieve_system_info()
        assert isinstance(result, str)

    def test_fetch_bios_info(self):
        result = AppLogic.fetch_bios_info()
        assert isinstance(result, str)

    def test_get_host_name(self):
        result = AppLogic.get_host_name()
        assert isinstance(result, str)
