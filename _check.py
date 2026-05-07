import ind_batch1
g = ind_batch1.INDUSTRIES_1[0]
print('General tools:', len(g['prompts']))
print('Coverage check:')
for t in g['prompts']:
    name = t['tool'][:38]
    pE = len(t['prompts'])
    pID = len(t.get('promptsID', []))
    pe = len(t.get('persona', []))
    pid_ = len(t.get('personaID', []))
    flag = '' if (pID >= pE and pe >= pE and pid_ >= pE) else ' <-- MISSING'
    print(f'  {name:40} EN={pE} ID={pID} per={pe} perID={pid_}{flag}')
