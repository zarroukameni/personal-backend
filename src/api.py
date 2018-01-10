import requests
from requests.exceptions import ConnectionError

# filter warnings, TODO this should be removed once we stop using self signed certs
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class BackendMycroftAPI(object):
    def __init__(self, api, lang="en-us", url="https://0.0.0.0:6712/v0.1/"):
        self.api = api
        self.headers = {"Authorization": str(self.api)}
        self.lang = lang
        self.url = url
        self.timeout = 10
        self.wait_time = 0.5

    def pair(self, code, uuid, name="jarbas"):
        ''' add a new user, requires admin api '''
        try:
            response = requests.put(
                self.url+"pair/"+code+"/"+uuid+"/"+name,
                headers=self.headers, verify=False
            )
            try:
                return response.json()
            except:
                print response.text
                raise ValueError("Invalid admin api key")
        except ConnectionError as e:
            raise ConnectionError("Could not connect: " + str(e))


if __name__ == "__main__":
    ap = BackendMycroftAPI("admin_key")
    name = "jarbas"
    print ap.pair("Q990Y8", "ff7bc301-d602-4eca-b31a-576337fb9685", name)

