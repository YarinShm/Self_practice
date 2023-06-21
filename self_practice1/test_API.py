from self_practice1.mainAPI import*

requests.get('https://jsonplaceholder.typicode.com/posts/1')

class TestAPI:

    def test_1_code(self):
       assert Check_status_code(code_side('https://jsonplaceholder.typicode.com/posts/1')) == True

    def test_2_content_type(self):
        assert response_headers_contain('https://jsonplaceholder.typicode.com/posts/1','application/json; charset=utf-8') == True

    def test_3_response_value_userid(self):
        assert does_it_valu('https://jsonplaceholder.typicode.com/posts/1', 1, 'userId') == True

    def test_4_response_value_title(self):
        assert does_it_valu_empty('https://jsonplaceholder.typicode.com/posts/1', 'title') == False

    def test_5_response_value_body(selfself):
        assert does_it_valu_empty('https://jsonplaceholder.typicode.com/posts/1', 'body') == False