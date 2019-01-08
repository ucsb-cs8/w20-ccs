import pytest

##############

from lab10 import midi2freq


def test_midi2freq_21():
    assert midi2freq(21)==pytest.approx(27.50,abs=1e-2)

def test_midi2freq_33():
    assert midi2freq(33)==pytest.approx(55.00,abs=1e-2)

def test_midi2freq_60():
    assert midi2freq(60)==pytest.approx(261.63,abs=1e-2)

def test_midi2freq_69():
    assert midi2freq(69)==pytest.approx(440.000,abs=1e-2)

def test_midi2freq_foo():
    with pytest.raises(ValueError):
       result = midi2freq("foo")

def test_midi2freq_n1():
    with pytest.raises(ValueError):
       result = midi2freq(-1)

def test_midi2freq_128():
    with pytest.raises(ValueError):
       result = midi2freq(128)

       
#############


from lab10 import spacedString

def test_spacedString_0():
    assert spacedString("",1)==""

def test_spacedString_1():
    assert spacedString("UCSB",1)=="U C S B"

    
def test_spacedString_2():
    assert spacedString("Cal Poly",2)=="C  a  l     P  o  l  y"

def test_spacedString_3():
    assert spacedString("UCSD",0)=="UCSD"

def test_spacedString_4():
   with pytest.raises(ValueError):
      result = spacedString("UCSD",-1)

def test_spacedString_5():
   with pytest.raises(ValueError):
      result = spacedString(["not a string"],0)

def test_spacedString_6():
   with pytest.raises(ValueError):
      result = spacedString("A String","Not an int")

def test_spacedString_7():
    assert spacedString("U",1)=="U"

def test_spacedString_8():
    assert spacedString("UC",1)=="U C"

def test_spacedString_9():
    assert spacedString(" A ",1)=="  A  "

def test_spacedString_10():
    assert spacedString("X X",1)=="X   X"

        
##########################

from lab10 import indicesOfEvens

def test_indicesOfEvens_0():
    assert indicesOfEvens([])==[]

def test_indicesOfEvens_1():
    assert indicesOfEvens([11,20,35,44,57,63,42])==[1,3,6]

def test_indicesOfEvens_2():
    assert indicesOfEvens([3,5,7,9])==[]    

def test_indicesOfEvens_3():
    assert indicesOfEvens([3,4,5])==[1]

def test_indicesOfEvens_4():
    assert indicesOfEvens([3,4,6])==[1,2]        
    
def test_indicesOfEvens_5():
    assert indicesOfEvens([4,3,4,6])==[0,2,3]        
    
def test_indicesOfEvens_6():
    with pytest.raises(ValueError):
      result = indicesOfEvens("foo")

def test_indicesOfEvens_7():
    with pytest.raises(ValueError):
      result = indicesOfEvens([4,5,"bar"])

###################################

from lab10 import countInRange

def test_countInRange_1():
    assert countInRange([10,20,30,40],20,30)==1

def test_countInRange_2():
    assert countInRange([10,20,30,40],20,40)==2

def test_countInRange_3():
    assert countInRange([10,20,30,40],10,41)==4

def test_countInRange_4():
    assert countInRange([10,20,30,40],0,10)==0    

def test_countInRange_5():
    assert countInRange([75,84,92,76,74,97,80,100,54],70,80)==3

def test_countInRange_6():
    with pytest.raises(ValueError):
      result = countInRange([4,5,"bar"],30,40)

def test_countInRange_7():
    with pytest.raises(ValueError):
      result = countInRange([4,5,6],"foo",40)

def test_countInRange_8():
    with pytest.raises(ValueError):
      result = countInRange([4,5,6],40,"bar")
    
def test_countInRange_9():
    with pytest.raises(ValueError):
      result = countInRange("foo",40,50)
