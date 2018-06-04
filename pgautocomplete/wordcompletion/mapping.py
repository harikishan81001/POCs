AUTOCOMPLETE_MAPPING = {
    "index_patterns":["*"],
    "settings":{
      "index.mapper.dynamic": True,
      "analysis": {
        "analyzer": {
            "autocomplete": {
                "tokenizer": "edge_ngram_tokenizer",
                "filter": [
                    "lowercase"
                ],
                "autocomplete_search" : {
                    "tokenizer" : "lowercase"
                  }
            },
        },
        "tokenizer": {
            "edge_ngram_tokenizer": {
                "type": "edge_ngram",
                "token_chars": ["letter", "digit"],
                "min_gram": 2,
                "max_gram": 20
            }
        }
    }
    },
    "mappings": {
        "warehouses": {
            "properties": {
                "suggest": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    },
                    "analyzer": "autocomplete"
                }
            },
            "dynamic_templates": [
              {
                "strings": {
                  "mapping": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                  },
                  "match": "*",
                  "match_mapping_type": "boolean"
                }
              }
            ],
        }
    }
}
