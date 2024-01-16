ERR_RESPONSES = {
    404 : {
            'status' : 404,
            'message' : 'not found',
            'body' : []
        },
    500 : {
            'status' : 500,
            'message' : 'server connection error',
            'body' : []
        },
    503 : {
            'status' : 503,
            'message' : 'service unavailable',
            'body' : []
        },
    401 : {
            'status' : 401,
            'message' : 'Unauthorized',
            'body' : []
        },
    403 : {
            'status' : 403,
            'message' : 'Forbidden',
            'body' : []
        },
    429 : {
            'status' : 429,
            'message' : 'Too Many Requests',
            'body' : []
        },
    502 : {
            'status' : 502,
            'message' : 'Bad Gateway',
            'body' : []
        },
}