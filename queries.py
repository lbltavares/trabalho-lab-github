queries = [
    #     {
    #         "questao": 1,
    #         "query": """
    # query questao1 {
    #   search(query: "stars:>10000", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         createdAt
    #         stargazers {
    #           totalCount
    #         }
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    #     {
    #         "questao": 2,
    #         "query": """
    # query questao2 {
    #   search(query: "stars:>10000", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         stargazers {
    #           totalCount
    #         }
    #         pullRequests(states: MERGED) {
    #           totalCount
    #         }
    #         mergeCommitAllowed
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    #     {
    #         "questao": 3,
    #         "query": """
    # query questao3 {
    #   search(query: "stars:>10000", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         createdAt
    #         stargazers {
    #           totalCount
    #         }
    #         releases(last: 10) {
    #           totalCount
    #           nodes {
    #             createdAt
    #           }
    #         }
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    #     {
    #         "questao": 4,
    #         "query": """
    # query questao4 {
    #   search(query: "stars:>10000", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         createdAt
    #         stargazers {
    #           totalCount
    #         }
    #         updatedAt
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    #     {
    #         "questao": 5,
    #         "query": """
    # query questao5 {
    #   search(query: "stars:>10000", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         stargazers {
    #           totalCount
    #         }
    #         languages(orderBy: {field: SIZE, direction: DESC}, first:1) {
    #           totalSize
    #           totalCount
    #           edges {
    #             size
    #             node {
    #               name
    #             }
    #           }
    #         }
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    #     {
    #         "questao": 6,
    #         "query": """
    # query questao6 {
    #   search(query: "stars:>10000 sort:stars", type: REPOSITORY, first: 100, after: %s) {
    #     nodes {
    #       ... on Repository {
    #         nameWithOwner
    #         createdAt
    #         closedIssues: issues(states: CLOSED) {
    #           totalCount
    #         }
    #         totalIssues: issues {
    #           totalCount
    #         }
    #       }
    #     }
    #     pageInfo {
    #       hasNextPage
    #       endCursor
    #       startCursor
    #     }
    #   }
    # }
    # """},
    {
        "questao": 7,
        "query": """
   query questao7 {
      search(query: "stars:>10000", type: REPOSITORY, first: 20, after: %s) {
        nodes {
          ... on Repository {
            nameWithOwner
            createdAt
            updatedAt
            stargazers {
              totalCount
            }
            releases(last: 10) {
              totalCount
            }
            languages(orderBy: {field: SIZE, direction: DESC}, first:1) {
              totalSize
              totalCount
              edges {
                size
                node {
                  name
                }
              }
            }
            pullRequests(states: MERGED) {
              totalCount
            }
            mergeCommitAllowed
          }
        }
        pageInfo {
          hasNextPage
          endCursor
          startCursor
        }
      }
    }
"""
    }
]
