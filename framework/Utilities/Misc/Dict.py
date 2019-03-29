class Dict:
    @staticmethod
    def flatten(current, key="", result={}):
        if isinstance(current, dict):
            for k in current:
                new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
                Dict.flatten(current[k], new_key, result)
        else:
            result[key] = current
        return result
