from urllib import response
import requests, json

openweathermap_API_KEY = "90b8455a3417ed83fff5fb4ee6da1118"
openweathermap_base_url = "https://api.openweathermap.org/data/2.5/weather?"
ipinfo_url = "https://ipinfo.io"

class Game(object):
    def __init__(self):
        pass

    def get_ip_info(self):
        response = requests.get(ipinfo_url)
        response_json = response.json()
        return response_json
    
    def cache_cases(self, method_name):
        raise NotImplementedError

    def reverse_string(self, string):
        string_cpy = [letter for letter in string] 
        i = 0
        j = len(string) - 1 lo
        while (i < j):
            temp = string_cpy[j]
            string_cpy[j] = string_cpy[i]
            string_cpy[i] = temp
            i += 1
            j -= 1
        return "".join(string_cpy)

    def step(self):
        input_arg = input("what next: ")
        match input_arg:
            case "dance":
                print("the type of input_arg is: {}".format(type(input_arg)))
            case "ipinfo":
                ip_info = self.get_ip_info()
                print(ip_info)
            case "ip_info":
                ip_info = self.get_ip_info()
                print(ip_info)
            case "ip info":
                ip_info = self.get_ip_info()
                print(ip_info)
            case "location":
                ip_info = self.get_ip_info()
                print("{}, {}, {}".format(
                    ip_info['city'],
                    ip_info['region'],
                    ip_info['country']
                ))
            case "reverse string":
                input_string = input("Enter string to be reversed: ")
                reversed_string = self.reverse_string(input_string)
                print("Your string reversed is: {}".format(reversed_string))
            case "detect palindrome":
                input_string = input("Enter string to be analyzed: ")
                reversed_string = self.reverse_string(input_string)
                if (input_string == reversed_string):
                    print("The inputted string is a palindrome.")
                else:
                    print("The inputted string is NOT a palindrome.")
            case "weather":
                ip_info = self.get_ip_info()
                openweathermap_url = openweathermap_base_url + "appid=" \
                    + openweathermap_API_KEY \
                    + "&q=" +  ip_info['city']
                response = requests.get(openweathermap_url)
                response_json = response.json()
                print(response_json)
            case "exit":
                exit()

if __name__== "__main__":
    game = Game()
    while (True):
        try:
            game.step()
        except KeyboardInterrupt:
            exit()
