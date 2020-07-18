import json
import pytest
import selenium.webdriver


@pytest.fixture
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ["Firefox","Chrome"]
    assert isinstance(config['implicit_wait'], int)
    assert config ['implicit_wait']>0

    return config

@pytest.fixture
def browser(config):
    if config['browser']=='Firefox':
        b = selenium.webdriver.Firefox("/Users/bellabaghdasaryan/Downloads/geckodriver")
    elif config['browser']== 'Chrome':
        b = selenium.webdriver.Chrome("/usr/local/bin/chromedriver")
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    b.implicitly_wait(config['implicit_wait'])

    yield b
    b.quit()

