from resources.page_objects import Amazon

test = Amazon()

test.launch_site()
test.search_for_an_item()
test.check_search_result()
test.close_session()