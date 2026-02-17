# Python 3 Eight-Character Encoder
An encoder that encodes arbitrary Python 3 code using eight distinct characters.

## Key Points
- Can encode arbitrary Python 3 code.
- No long sequences of '%'s.

## Usage
Pass the file containing the original Python 3 code as argv\[1\].

## Example
```Python
# original
print('Hello, world!')

# encoded
exec('c=%x'%(''=='%'))==exec('e=%x'%(''==''))==exec('cex=%x%%x'%e%e)==exec('ec=%x%%x%%%%x%%%%%%%%x'%c%cex%e%e)==exec('ee=%x%%x%%%%x%%%%%%%%x%%%%%%%%%%%%%%%%x'%c%cex%e%c%c)==exec('ece=%x%%x'%ee%ec)==exec('''cx=('%c')'''%ece)==exec('x=%x%%c%%%%x'%e%cx%e)==exec('ex=%x%%c%%%%x'%ee%cx%e)==exec('xc=%x%%c%%%%x'%ex%cx%e)==exec('xe=%x%%c%%%%x'%xc%cx%e)==exec('xx=%x%%c%%%%x'%xe%cx%e)==exec('ecc=%x%%c%%%%x'%xx%cx%e)==exec('ecx=%x%%x'%ecc%x)==exec('''cec=('%c%%c')'''%ecx%ecx)==exec('eee=%x%%x%%%%x'%e%e%c)==exec('''cee=('%c')'''%eee)==exec('''cc=('')''')==exec('''ce=('%c%%c%%%%c%%%%%%%%c%%%%%%%%%%%%%%%%c')''')==exec('''cxc=('%c')''')==exec('''cxe=('%c%%c')''')==exec('''cxx=('%c%%c%%%%c')''')==exec('''ccc=('%c%%c%%%%c%%%%%%%%c')''')==exec('ece=%x%%x'%ee%c)==exec('ecx=%x%%x%%%%x'%e%c%c)==exec('eec=%x%%x'%ec%ec)==exec('eee=%x%%x%%%%x'%e%c%e)==exec('eex=%x%%x'%ee%e)==exec('exc=%x%%x%%%%x'%e%e%ee)==exec('exe=%x%%x%%%%x'%e%e%xc)==exec('exx=%x%%x'%ee%ee)==exec('xcc=%x%%x%%%%x'%e%e%e)==exec('xce=%x%%x'%ec%ecc)==exec('xcx=%x%%x%%%%x'%e%c%ex)==exec('xec=%x%%x%%%%x'%e%c%xx)==exec('xee=%x%%x'%xe%x)==exec('xex=%x%%x%%%%x'%e%e%x)==exec('xxc=%x%%x'%ec%x)==exec('xxe=%x%%x%%%%x'%e%e%ecc)==exec('cc%c=ce%%xex%%exc%%xcx%%cee%%exe'%cx)==exec('cc%c=ce%%ece%%xce%%xee%%eee%%xec'%cx)==exec('cc%c=ce%%xec%%xcc%%exx%%xxc%%xxe'%cx)==exec('cc%c=ce%%xcc%%exc%%xec%%ecx%%eec'%cx)==exec('cc%c=cxe%%xce%%eex'%cx)==exec(cc)
```

## Details
- Constructs numbers 0-9 before building Unicode values.
- Names variables using a ternary system.
- Uses '==' instead of '\n'.
- Concatenates at most five letters at once.

## License
BSD 3-Clause
