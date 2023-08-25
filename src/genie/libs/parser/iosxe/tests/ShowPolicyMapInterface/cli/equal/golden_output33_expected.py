expected_output = {
    "Port-channel10":{
        "service_policy":{
            "input":{
                "policy_name":{
                    "map1":{
                        "class_map":{
                            "cs1":{
                                "match_evaluation":"match-all",
                                "packets":0,
                                "match":[
                                    "dscp cs1 (8)"
                                ],
                                "police":{
                                    "rate_bps":1000000000,
                                    "burst_bytes":1024000,
                                    "conformed":{
                                        "bytes":0,
                                        "actions":{
                                            "transmit":True
                                        },
                                        "bps":0
                                    },
                                    "exceeded":{
                                        "bytes":0,
                                        "actions":{
                                            "drop":True
                                        },
                                        "bps":0
                                    }
                                }
                            },
                            "cs5":{
                                "match_evaluation":"match-all",
                                "packets":0,
                                "match":[
                                    "dscp cs5 (40)"
                                ],
                                "police":{
                                    "rate_bps":100000000,
                                    "burst_bytes":10240,
                                    "conformed":{
                                        "bytes":0,
                                        "actions":{
                                            "transmit":True
                                        },
                                        "bps":0
                                    },
                                    "exceeded":{
                                        "bytes":0,
                                        "actions":{
                                            "drop":True
                                        },
                                        "bps":0
                                    }
                                }
                            },
                            "aclv4":{
                                "match_evaluation":"match-all",
                                "packets":396221,
                                "match":[
                                    "access-group name aclv4"
                                ],
                                "police":{
                                    "rate_bps":100000000,
                                    "burst_bytes":10240,
                                    "conformed":{
                                        "bytes":196680000,
                                        "actions":{
                                            "transmit":True
                                        },
                                        "bps":4898000
                                    },
                                    "exceeded":{
                                        "bytes":1784425000,
                                        "actions":{
                                            "drop":True
                                        },
                                        "bps":44416000
                                    }
                                }
                            },
                            "class-default":{
                                "match_evaluation":"match-any",
                                "packets":396231,
                                "match":[
                                    "any"
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}