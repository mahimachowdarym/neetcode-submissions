class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "[]"
        return "é".join(strs,)

    def decode(self, s: str) -> List[str]:
        if s=="[]":
            return []
        return list(s.split("é"))
