# SLCB Dictionary APIs

Adds parameters for various dictionary apis to allow for getting word info in custom commands. 

## Installing

This script was built for use with Streamlabs Chatbot.
Follow instructions on how to install custom script packs at:
https://github.com/StreamlabsSupport/Streamlabs-Chatbot/wiki/Prepare-&-Import-Scripts

Click [Here](https://github.com/Encrypted-Thoughts/SLCB-DictionaryAPI/blob/master/DictionaryAPI.zip?raw=true) to download the script pack.

In order to use this script to get data from WordsAPI or Urban Dictionary you'll need to have an account with Rapid API. <br />

WordsAPI: <br />
You can register for a Free tier at the below link that will allow 2500 requests a day and charge $0.004 per request after that. <br />
https://rapidapi.com/dpventures/api/wordsapi/pricing 

Once registered you'll need to find your api key and enter it into the script settings. <br />
https://rapidapi.com/dpventures/api/wordsapi/endpoints

Urban Dictionary: <br />
Same steps are with Words API except it has unlimited free requests. <br />
https://rapidapi.com/community/api/urban-dictionary

![image](https://user-images.githubusercontent.com/50642352/85881019-8f996080-b7a2-11ea-8d4a-f95d019bde34.png)

![image](https://user-images.githubusercontent.com/50642352/85881103-b8b9f100-b7a2-11ea-86a6-ba317c46196e.png)

## Use

Once installed the below parameter can be inserted into custom commands created in SLCB.
In custom script parameters a character length on definition can be set.
This allows long definitions to be limited so the bot doesn't spam chat with multiple messages.

```
$google(
    string   # Word: The word that the parameter should retrieve the definition.,
    string   # Format String: the format the response will be returned in. 
             # Ex: {word} {pronunciation} : {origin} : {definitions}
             # EX: {word} {pronunciation} : {origin} : {definition_n} Ex: {example_n}
)

Example Command: !command add !define $google($msg, {word} {pronunciation} : {origin} : {definitions})
Example Command: !command add !define $google($msg, {word} {pronunciation} : {origin} : {definition_1} Ex: {example_1})
```
```
$wordsapi(
    string   # Word: The word that the parameter should retrieve the definition.,
    string   # Format String: the format the response will be returned in. 
             # Ex: {word} {pronunciation}: {definitions}
)

Example Command: !command add !define $wordsapi($msg, {word} {pronunciation}: {definitions})
```
```
$urban(
    string   # Word: The word that the parameter should retrieve the definition.,
    string   # Format String: the format the response will be returned in. 
             # Ex: {word}: {definition} {link} {thumbs_up} {thumbs_down} {timestamp} {author} {example}
)

Example Command: !command add !define $urban($msg, {word}: {definition} {link} {thumbs_up} {thumbs_down} {timestamp} {author} {example})
```

Examples in twitch chat:

![image](https://user-images.githubusercontent.com/50642352/85969733-19f1e800-b98e-11ea-998d-2904a9b20b58.png)
<br/>
![image](https://user-images.githubusercontent.com/50642352/85913422-483ebe80-b7fa-11ea-837f-e94690023a7d.png)
<br/>
![image](https://user-images.githubusercontent.com/50642352/85913344-a7500380-b7f9-11ea-8629-6874b6e0f031.png)

## Author

EncryptedThoughts - [Twitch](https://www.twitch.tv/encryptedthoughts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

