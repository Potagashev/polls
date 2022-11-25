from fastapi import HTTPException

NOT_VOTED_RESPONSE_403 = HTTPException(
    status_code=403,
    detail='You did not voted this poll to see its results'
)

ALREADY_VOTED_403 = HTTPException(
    status_code=403,
    detail='You have already voted this poll'
)
