from agent import run_agent
if __name__=='__main__':
    question=input('Ask ResearchMate: ')
    response=run_agent(question)
    print('Answer:',response['answer'])
    print('Tools used:',response['trace'])