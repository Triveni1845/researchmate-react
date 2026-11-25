from tools import calculate, search_documents
REGISTRY={'calculate':calculate,'search_documents':search_documents}
def dispatch(name,args):
    if name not in REGISTRY: return {'error':'not_allowed'}
    try: return REGISTRY[name](**args)
    except (TypeError,ValueError) as e: return {'error':'invalid_args','detail':str(e)}