GET_USER_THRESHOLDS_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "accounts": {
          "type": "object",
          "properties": {
            "getOne": {
              "type": "object",
              "properties": {
                "__typename": {
                  "type": "string"
                },
                "thresholds": {
                  "type": "object",
                  "properties": {
                    "temperature": {
                      "type": "object",
                      "properties": {
                        "min": {
                          "type": "integer"
                        },
                        "max": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "min",
                        "max"
                      ]
                    },
                    "pulse": {
                      "type": "object",
                      "properties": {
                        "min": {
                          "type": "integer"
                        },
                        "max": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "min",
                        "max"
                      ]
                    },
                    "pressureSystolic": {
                      "type": "object",
                      "properties": {
                        "min": {
                          "type": "integer"
                        },
                        "max": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "min",
                        "max"
                      ]
                    },
                    "pressureDiastolic": {
                      "type": "object",
                      "properties": {
                        "min": {
                          "type": "integer"
                        },
                        "max": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "min",
                        "max"
                      ]
                    },
                    "alcohol": {
                      "type": "object",
                      "properties": {
                        "min": {
                          "type": "integer"
                        },
                        "max": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "min",
                        "max"
                      ]
                    }
                  },
                  "required": [
                    "temperature",
                    "pulse",
                    "pressureSystolic",
                    "pressureDiastolic",
                    "alcohol"
                  ]
                }
              },
              "required": [
                "__typename",
                "thresholds"
              ]
            }
          },
          "required": [
            "getOne"
          ]
        }
      },
      "required": [
        "accounts"
      ]
    }
  },
  "required": [
    "data"
  ]
}