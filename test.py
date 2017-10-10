def test_example(selenium):
  selenium.get('localhost:8080')
  # this test will pass
  assert selenium.title == 'Check this title'
  # this test will fail
  assert selenium.title == 'Nothing'
