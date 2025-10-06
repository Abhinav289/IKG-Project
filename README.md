# IKG Project

## Description

### Part 1
1. Gather new textual data (with dates) regarding a domain (topic) of your choice from a social media of your choice.
2. Do the analysis of the data in terms of the relevance of the content and link structure as studied and mention in the report.
3. Also, measure the effectiveness of your methodology by evaluating the method you have used and mention in the report.

### Part 2
1. Construct a knowledge graph from the data that you have gathered. 
2. Mention all the methods you have used to construct the knowledge graph. 
3. Your analysis of the knowledge graph construction methods should be mentioned in the report, and the actual knowledge graph also should be submitted.

## Twitter API
https://twitterapi.io/

### Advanced Search Tweet End Point
https://docs.twitterapi.io/api-reference/endpoint/tweet_advanced_search

```python
import requests
url = "https://api.twitterapi.io/twitter/tweet/advanced_search"
headers = {"X-API-Key": "<api-key>"}
response = requests.get(url, headers=headers)
print(response.json())
```

200 response
```json
{
  "tweets": [
    {
      "type": "tweet",
      "id": "<string>",
      "url": "<string>",
      "text": "<string>",
      "source": "<string>",
      "retweetCount": 123,
      "replyCount": 123,
      "likeCount": 123,
      "quoteCount": 123,
      "viewCount": 123,
      "createdAt": "<string>",
      "lang": "<string>",
      "bookmarkCount": 123,
      "isReply": true,
      "inReplyToId": "<string>",
      "conversationId": "<string>",
      "displayTextRange": [
        123
      ],
      "inReplyToUserId": "<string>",
      "inReplyToUsername": "<string>",
      "author": {
        "type": "user",
        "userName": "<string>",
        "url": "<string>",
        "id": "<string>",
        "name": "<string>",
        "isBlueVerified": true,
        "verifiedType": "<string>",
        "profilePicture": "<string>",
        "coverPicture": "<string>",
        "description": "<string>",
        "location": "<string>",
        "followers": 123,
        "following": 123,
        "canDm": true,
        "createdAt": "<string>",
        "favouritesCount": 123,
        "hasCustomTimelines": true,
        "isTranslator": true,
        "mediaCount": 123,
        "statusesCount": 123,
        "withheldInCountries": [
          "<string>"
        ],
        "affiliatesHighlightedLabel": {},
        "possiblySensitive": true,
        "pinnedTweetIds": [
          "<string>"
        ],
        "isAutomated": true,
        "automatedBy": "<string>",
        "unavailable": true,
        "message": "<string>",
        "unavailableReason": "<string>",
        "profile_bio": {
          "description": "<string>",
          "entities": {
            "description": {
              "urls": [
                {
                  "display_url": "<string>",
                  "expanded_url": "<string>",
                  "indices": [
                    123
                  ],
                  "url": "<string>"
                }
              ]
            },
            "url": {
              "urls": [
                {
                  "display_url": "<string>",
                  "expanded_url": "<string>",
                  "indices": [
                    123
                  ],
                  "url": "<string>"
                }
              ]
            }
          }
        }
      },
      "entities": {
        "hashtags": [
          {
            "indices": [
              123
            ],
            "text": "<string>"
          }
        ],
        "urls": [
          {
            "display_url": "<string>",
            "expanded_url": "<string>",
            "indices": [
              123
            ],
            "url": "<string>"
          }
        ],
        "user_mentions": [
          {
            "id_str": "<string>",
            "name": "<string>",
            "screen_name": "<string>"
          }
        ]
      },
      "quoted_tweet": {},
      "retweeted_tweet": {},
      "isLimitedReply": true
    }
  ],
  "has_next_page": true,
  "next_cursor": "<string>"
}
```

400 response
```json
{
  "error": 123,
  "message": "<string>"
}
```

## Queries
```python
"\"reinforcement learning\" OR \"RL\" OR \"deep RL\" OR \"DQN\" OR \"reward function\" lang:en from:HuggingPapers"
```
```python
"\"diffusion\" lang:en from:HuggingPapers"
```