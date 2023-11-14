import random

def mine_block(p):
    miners = ["honest", "attacker"]
    result = random.choices(miners, weights=[1-p, p])[0]
    return result

def egoistic_miner_strategy(p, rounds):
    honest_blocks_mined = 0
    attacker_blocks_mined = 0 

    honest_rewards = 0
    attacker_rewards = 0


#A round is one full transition (return to state 0)
    for i in range(rounds):
        round_finished = False
        state = 0

        #A round is finished when the state returns to 0
        while round_finished != True:
            match state:
                #We start at the first state
                case 0:
                    #If the honest miner mines first, we start the round again
                    if mine_block(p) == "honest":
                        honest_blocks_mined+=1
                        round_finished = True

                    #Else, the state goes to 1
                    else:
                        state = 1

                case 1:
                    #If the honest block finds a block, there is a competition (state 0' (or 3))
                    if mine_block(p) == "honest":
                        state = "competition"

                    #Else, the state goes to 2
                    else:
                        state = 2

                case 2:
                    #If the honest block finds a block, then the attacker publishes his 2 blocks and earns 2 rewards (case A, A, B)
                    if mine_block(p) == "honest":
                        attacker_blocks_mined+=2
                        round_finished = True
                    #Else, the attacker publishes his version of the blockchain and earns 3 rewards (case A, A, A)
                    else:
                        state+=1

                case "competition":
                    #If the honest miner finds a block, he publishes 2 blocks and earns 2 rewards (case A, B, B)
                    if mine_block(p) == "honest":
                        honest_blocks_mined+=2
                        round_finished = True
                    #Else, the attacker publishes his version of the blockchain and earns 2 rewards (case, A, B, A)
                    else:
                        attacker_blocks_mined+=2
                        round_finished = True

                case _:
                    if mine_block(p) == "honest":
                        state-=1
                        attacker_blocks_mined+=1
                    else:
                        state+=1

    return (f"Honest Blocks Mined : {honest_blocks_mined}, Attacker Blocks Mined : {attacker_blocks_mined}, Probability of winning Attack : {attacker_blocks_mined/(honest_blocks_mined+attacker_blocks_mined)}")


print(egoistic_miner_strategy(0.45, 5000))