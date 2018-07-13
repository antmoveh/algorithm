
# 二进制转行实现
# bin()、oct()、int()、hex()

"""
1. Varint编码
数据传输中出于IO的考虑，我们会希望尽可能的对数据进行压缩。
Varint就是一种对数字进行编码的方法，编码后二进制数据是不定长的，数值越小的数字使用的字节数越少。
实际场景中小数字的使用远远多于大数字，因此通过Varint编码对于大部分场景都可以起到一个压缩的效果。

编码规则：
最高位(most significant bit)表示编码是否继续，如果该位为1，表示接下来的字节仍然是该数字的一部分，如果该位为0，表示编码结束。字节里的其余7位用原码补齐，采用低位字节补齐到高位的办法。
举几个数值具体说明下编码规则：

对数字1进行varint编码后的结果为0000 0001，占用1个字节。相比int32的数字1存储占用4个字节，节省了3个字节的空间（主要是高位的0），而Varint的想法就是以标志位替换掉高字节的若干个0。
对数字300进行varint编码，原码形式为：
00000000 00000000 00000001 00101100
编码后的数据：第一个字节为10101100，第二个字节为00000010（不够7位高位补0）。

ZigZag是将有符号数统一映射到无符号数的一种编码方案，对于无符号数0 1 2 3 4，映射前的有符号数分别为0 -1 1 -2 2，负数以及对应的正数来回映射到从0变大的数字序列里
uint32  return (n << 1) ^ (n >> 31);
int32  return (n >> 1) ^ -static_cast<int32>(n & 1);
uint64 return (n << 1) ^ (n >> 63);
int64 return (n >> 1) ^ -static_cast<int64>(n & 1);
pb从经验出发使用varint编码，整型只需要int32/int64/uint32/uint64就可以了，一般不需要考虑编码后的大小。
"""


class VarInt(object):

    @classmethod
    def _zigzag_encode(cls, num):
        retval = num * 2 if num >= 0 else -2 * num - 1
        return int(retval)

    @classmethod
    def _zigzag_decode(cls, num):
        retval = - (num + 1) / 2 if num % 2 else num / 2
        return int(retval)

    @classmethod
    def int_to_var(cls, num):
        num = cls._zigzag_encode(num)
        front = rear = count = 0
        while True:
            if num >> 7:
                temp = num & 0x7f
                if rear:
                    rear += (temp | 0x80) << 8
                else:
                    rear = temp
                count += 1
                num >>= 7
            else:
                front = num
                break
            if count:
                front = (front | 0x80) << count * 8
            return front + rear

    @classmethod
    def var_to_int(cls, num):
        front = rear = count = 0
        while True:
            if num >> 8:
                temp = num & 0x7f
                if rear:
                    rear |= temp << 7
                else:
                    rear = temp
                count += 1
                num >>= 8
            else:
                front = num & 0x7f
                break
            if count:
                front <<= count * 7
            return cls._zigzag_decode(front + rear)


if __name__ == "__main__":
    import random
    v = random.choice([5, -3])
    x1 = VarInt._zigzag_encode(v)
    print(x1)
    x2 = VarInt._zigzag_decode(x1)
    print(x2)