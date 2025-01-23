def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default="https://rozetka.com.ua", help="TEST BASE URL")
