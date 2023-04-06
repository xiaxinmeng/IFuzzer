from typing import List, Dict, NoReturn

def get_profile_a(user_id: int, likes: Dict[str, int]) -> Dict[str, int]:
    return {'user_id': user_id, 'likes': len(likes.keys())}

if __name__ == "__main__":
    get_profile_a()