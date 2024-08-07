
import BingImageCreator
from os import system,listdir
from head.ucookie import u_cookie_value

# cookie = '1q02owQZ_hdSCI2IaDapR6DiabD9P8IEDYk92QKWlu0Q66dEKQiUEssBuJCsHGu3VwpmgH8DngSbTmh26LaTd6YiD-TrHR8CnQCTw4akYOxIZI5PjD0p54rxtYPfAz9YOCyBv5V2rStqeggw0VVin8C3Jl6E4EGj5OXJXlzSsUOHo9Z0udG8-7QKIOzewBF_FjZzDcRNG2Lrf9mPbq2PckeHVJkh-pDT4jTk6moLKJvY'
# cookie = '1LywfRibWKKTTI7oucHhMiggqWf9Ow7xLB7s7mgE7fqm0449YjT7L_Lbtni673ctDe_DVKoj1Gm2HjhCiNN34LcvoZY6GzC0C8RDo4IyuGcpzMnA3bn5BPmkr0jL6qE1rIVpuBL4pvwvc9xvdo5wPUl6aekT-JlxY7Ew9vvTW_Z5pdnww9xfK86Fs2bVun30hI9RCznOxSpc5KfGGGDX-arqn-YWLi8_REhnaZOL6J9w'

def generate_image(prompt):
    
        
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{u_cookie_value}"')
    return listdir('output')

images = generate_image('demon slayer ')
print(images)
