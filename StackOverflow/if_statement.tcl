set A {50 98 76 34 67}
set B {12 23 48 59 65}

foreach c $A d $B {
    if {30 <= $c && $c <= 60} {
        puts $c
    } 
    
    if {20 <= $d && $d <= 30} {
        puts $d
    }
}
