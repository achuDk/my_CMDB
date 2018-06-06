#!/usr/bin/env python
# -*- coding:utf-8 -*-


from test_Agent_with_plugins.src import script

if __name__ == '__main__':
    response = script.AgentClient().run()
    print('response : ',response)

    # import time
    # # 如果响应为ok，则过一会执行
    # if response == 'ok':
    #     time.sleep(10)
    #     response = script.Agent().run()
    # else:
    # # 如果响应不为ok，则立刻重新执行
    #     response = script.Agent().run()
    #     print(response)
