import sys
from collections import deque

def log(message):
    print(message, flush=True)

class Stack:
    def __init__(self):
        self.stack = deque()
 
    def push(self, item):
        # 添加一个新的元素到栈顶
        self.stack.append(item)
 
    def pop(self):
        # 移除并返回栈顶的元素
        return self.stack.pop()
 
    def peek(self):
        # 返回栈顶的元素，但不移除它
        return self.stack[-1] if self.stack else None
 
    def is_empty(self):
        # 判断栈是否为空
        return not self.stack
 
    def size(self):
        # 返回栈的元素个数
        return len(self.stack)
    
    def all(self):
        # 返回所有栈内元素
        return self.stack

def main():
    log("Starting...")

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    log("inputPath: " + inputPath)
    log("outputPath: " + outputPath)

    with open(outputPath, 'w') as outPutFile:

        itemStatus = 0
        stack = Stack()

        isError = False

        with open(inputPath, 'r') as inputFile:

            itemJson = ""

            rowNum = 0

            # 逐行读取
            for line in inputFile.readlines():

                rowNum = rowNum + 1

                lineStrip = line.strip()

                colNum = 0

                """
                逐字符分析，
                1. 遇到 '{' 和 '[' 入栈；
                2. 遇到 '}' 和 ']' 出栈；
                3. 根据 itemStatus == 0 判断一个 item 的开始；
                4. 根据栈为空判断一个 item 的结束。
                """

                for char in lineStrip:

                    colNum = colNum + 1

                    if itemStatus == 0:

                        """
                        itemStatus == 0，标志着一个 item 的开始，此时期待一个 '{'
                        """

                        if char == '{':
                            # 入栈
                            stack.push(char)

                            # 一个 item 开始了
                            itemStatus = 1

                            itemJson = char
                    
                    elif itemStatus == 1:
                        
                        """
                        itemStatus == 1，代表正在一个 item 内，
                        1. 遇到 '{' 和 '[' 入栈；
                        2. 遇到 '}' 和 ']' 出栈；
                        3. 遇到 '}'、'{' 出栈后，如果栈内为空，则证明一个 item 结束了。
                        """

                        itemJson = itemJson + char

                        if char == '{' or char == '[':
                            # 入栈
                            stack.push(char)
                        elif char == '}':
                            if stack.peek() == '{':

                                # 出栈
                                stack.pop()

                                if stack.is_empty():

                                    # 当前 item 结束了，一个新的 item 将开始
                                    itemStatus = 0

                                    # 将当前 item 写到输出文件
                                    outPutFile.write(itemJson + '\n')
                            else:
                                log("Invalid JSON: '{' is expected on stack top, but received '" + stack.peek() + "'(line: " + str(rowNum) + ", column: " + str(colNum) + ").")
                                log("stack:")
                                log(stack.all())
                                isError = True
                                break;
                        elif char == ']':
                            if stack.peek() == '[':

                                # 出栈
                                stack.pop()
                                
                            else:
                                log("Invalid JSON: '[' is expected on stack top, but received '" + stack.peek() + "'(line: " + str(rowNum) + ", column: " + str(colNum) + ").")
                                log("stack:")
                                log(stack.all())
                                isError = True
                                break;
                
                if isError:
                    log("Error:")
                    log("Line:")
                    log(line)
                    break;
        
    log("Starting...Done.")


if __name__ == '__main__':
    main()
