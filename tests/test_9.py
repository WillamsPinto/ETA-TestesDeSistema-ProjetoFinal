class Test5:

    @pytest.mark.suite5
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_search_product(self, open_home_all_browsers):