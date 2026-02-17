import sys


def ternary(n):
    if n < 3:
        return str(n)
    n, r = divmod(n, 3)
    return ternary(n) + str(r)

def get_name():
    n = 9
    while True:
        n += 2 if n == 47 else 1
        yield ternary(n).replace('0', 'c').replace('1', 'e').replace('2', 'x')


gen_name = get_name()
nums = {'0': 'c', '1': 'e', '2': 'x', '3': 'ec', '4': 'ee', '5': 'ex', '6': 'xc', '7': 'xe', '8': 'xx', '9': 'ecc'}
names = {'+': 'cx', '\\': 'cec', 'n': 'cee'}
blocks = ['cxc', 'cxe', 'cxx', 'ccc', 'ce']
output = "exec('c=%x'%(''=='%'))==exec('e=%x'%(''==''))==exec('cex=%x%%x'%e%e)==exec('ec=%x%%x%%%%x%%%%%%%%x'%c%cex%e%e)==exec('ee=%x%%x%%%%x%%%%%%%%x%%%%%%%%%%%%%%%%x'%c%cex%e%c%c)==exec('ece=%x%%x'%ee%ec)==exec('''cx=('%c')'''%ece)==exec('x=%x%%c%%%%x'%e%cx%e)==exec('ex=%x%%c%%%%x'%ee%cx%e)==exec('xc=%x%%c%%%%x'%ex%cx%e)==exec('xe=%x%%c%%%%x'%xc%cx%e)==exec('xx=%x%%c%%%%x'%xe%cx%e)==exec('ecc=%x%%c%%%%x'%xx%cx%e)==exec('ecx=%x%%x'%ecc%x)==exec('''cec=('%c%%c')'''%ecx%ecx)==exec('eee=%x%%x%%%%x'%e%e%c)==exec('''cee=('%c')'''%eee)==exec('''cc=('')''')==exec('''ce=('%c%%c%%%%c%%%%%%%%c%%%%%%%%%%%%%%%%c')''')==exec('''cxc=('%c')''')==exec('''cxe=('%c%%c')''')==exec('''cxx=('%c%%c%%%%c')''')==exec('''ccc=('%c%%c%%%%c%%%%%%%%c')''')"

with open(sys.argv[1], encoding='UTF-8') as f_in:
    text = f_in.read()
    symbols = set(text) - names.keys()

for symbol in symbols:
    var = ctt = ''
    for i, num in enumerate(str(ord(symbol))):
        var += '%'*2**i + 'x'
        ctt += '%' + nums[num]
    names.update({symbol: (name := next(gen_name))})
    output += f"==exec('{name}={var}'{ctt})"

block = ''
i = j = 0
length = len(text)
while i < length:
    block += f'%%{names[symbol := text[i]]}'
    i += 1
    j += 1
    if j == 5 or symbol == '%' or i == length:
        output += f"==exec('cc%c={blocks[j-1]}{block}'%cx)"
        block = ''
        j = 0

with open('output.py', 'w', encoding='UTF-8') as f_out:
    f_out.write(output + '==exec(cc)')