import math
import sys

loop = True
while loop == True:
        def PolygonFormulas(userinput):

                if userinput == 13:

                        A = float(input("What is the measure of the area?"))
                        dOne = float(input("What is the measure of the second diagonal?"))

                        TwoA = A * 2
                        
                if userinput == 12:
                        
                        A = float(input("What is the area of the kite?"))
                        dTwo = float(input("What is the measure of the second diagonal?"))

                        TwoA = 2 * A
                        dOne = TwoA / dTwo
                        print("The measure of the first diagonal is %.2f" %dOne)

                        print("Here is the process: ")
                        print("2A / d2 = d1")
                        print("2(%.2f) / %.2f = d1" % (A,dTwo))
                        print("%.2f / %.2f = d1" % (TwoA,dTwo))
                        print("%.2f = d1" %dOne)

                if userinput == 11:

                        dOne = float(input("What is the measure of the first diagonal?"))
                        dTwo = float(input("What is the measure of the second diagonal?"))

                        dThree = dOne * dTwo
                        A = dThree / 2
                        print("The area the diagonal is %.2f" %A)

                        print("Here is the process: ")
                        print("A = (d1 * d2) / 2")
                        print("A = (%.2f * %.2f) / 2" % (dOne,dTwo))
                        print("A = %.2f / 2" %dThree)
                        print("A = %.2f" %A)

                if userinput == 10: 
                
                        A = float(input("What is the area of the trapezoid?"))
                        h = float(input("What is the height of the trapezoid?"))
                        bTwo = float(input("What is the measure of the second base?"))

                        Halfh = h / 2
                        ADiv = A / Halfh
                        bOne = ADiv - bOne
                        print("The measure of the second base is %.2f" %bTwo)

                        print("Here is the process: ")
                        print("A / 1/2h - b1 = b1")
                        print("%.2f / 1/2(%.2f) - %.2f = b1" % (A,h,bTwo))
                        print("%.2f / %.2f - %.2f = b1" % (A,Halfh,bTwo))
                        print("%.2f - %.2f = b1" % (Adiv,bTwo))
                        print("%.2f = b1" %bOne)

                if userinput == 9: 

                        A = float(input("What is the area of the trapezoid?"))
                        h = float(input("What is the height of the trapezoid?"))
                        bOne = float(input("What is the measure of the first base?"))

                        Halfh = h / 2
                        ADiv = A / Halfh
                        bTwo = ADiv - bOne
                        print("The measure of the second base is %.2f" %bTwo)

                        print("Here is the process: ")
                        print("A / 1/2h - b1 = b2")
                        print("%.2f / 1/2(%.2f) - %.2f = b2" % (A,h,bOne))
                        print("%.2f / %.2f - %.2f = b2" % (A,Halfh,bOne))
                        print("%.2f - %.2f = b2" % (ADiv,bOne))
                        print("%.2f = b2" %bTwo)

                if userinput == 8: 

                        A = float(input("What is the area of the trapezoid?"))
                        bOne = float(input("What is the measure of the first base of the trapezoid?"))
                        bTwo = float(input("What is the measure of the second base of the triangle?"))

                        Sum = bOne + bTwo
                        SumDivA = A / Sum
                        h = SumDivA * 2
                        print("The height of the trapezoid is %.2f" %h)

                        print("Here is the process :")
                        print("(A / b1 + b2) * 2 = h")
                        print("(%.2f / %.2f + %.2f) * 2 = h" % (A,bOne,bTwo))
                        print("(%.2f / %.2f) * 2 = h" % (A,Sum))
                        print("%.2f * 2 = h" %SumDivA)
                        print("%.2f = h" %h)
                              
                if userinput == 7:

                        h = float(input("What is the height of the trapezoid?"))
                        bOne = float(input("What is the measure of the first base?"))
                        bTwo = float(input("What is the measure of the second base?"))

                        Halfh = h / 2
                        FirstPar = bOne + bTwo
                        A = Halfh * FirstPar
                        print("The area of the trapezoid is %.2f" %A)

                        print("Here is the process: ")
                        print("A = 1/2h(b1 + b2)")
                        print("A = 1/2(%.2f)(%.2f + %.2f)" % (h,bOne,bTwo))
                        print("A = %.2f(%.2f)" % (Halfh,FirstPar))
                        print("A = %.2f" %A)

                if userinput == 6:

                        A = float(input("What is the area of the triangle?"))
                        B = float(input("What is the base of the triangle?"))

                        TwoA = 2 * A
                        H = TwoA / B
                        print("The height of the triangle is %.2f" %H)

                        print("Here is the process: ")
                        print("2A / b = h")
                        print("2(%.2f )/ %.2f = H" %(A,B))
                        print("%.2f / %.2f = h" % (TwoA,B))
                        print("%.2f = h" %H)
                        
                if userinput == 5: 

                        A = float(input("What is the area of the triangle?"))
                        H = float(input("What is the height of the triangle?"))

                        TwoA = 2 * A
                        B = TwoA / H
                        print("The height of the triangle is %.2f" %B)

                        print("Here is the process: ")
                        print("2A/b = h")
                        print("2(%.2f)/%.2f = h" %(A,H))
                        print("%.2f/%.2f = h" %(TwoA,H))
                        print("%.2f = h" %B)
                        
                if userinput == 4:
                        B = float(input("What is the base of the triangle?"))
                        H = float(input("What is the height of the triangle?"))

                        BH = B * H
                        A = BH / 2
                        print("The area of the triangle is %.2f" %A)

                        print("Here is the process: ")
                        print("A = 1/2BH")
                        print(" A = 1/2(%.2f)(%.2f)" % (B,H))
                        print("A = 1/2(%.2f)" %BH)
                        print("A = %.2f" %A)
                          
                if userinput == 3:

                        A = float(input("What is the area of the rectangle?"))
                        H = float(input("What is the height of the rectangle?"))

                        B = A / H
                        print("The base of the rectangle based on the area and the height is %.2f" %B)
                        print("Here is the process: ")
                        print(" B = A / H")
                        print(" B = %.2f/%.2f" % (A,H))
                        print(" B = %.2f" %H)
                
                if userinput == 2:

                        A = float(input("What is the area of the rectangle?"))
                        B = float(input("What is the base of the rectangle?"))

                        H = A / B
                        print("The Height of the rectangle based on the area and base is %.2f" %H)
                        print("Here is the process: ")
                        print("H = A/B")
                        print("H = %.2f/%.2f" %(A,B))
                        print("H = %.2f" %H)
                                  
                if userinput == 1:
                        B = float(input("What is the base of the rectangle?"))
                        H = float(input("What is the height of the triangle?"))

                        A = B * H
                        print("The area of the rectangle is %.2f" %A)

                        print("Here is the process: ")
                        print("A = BH")
                        print("A = %.2f(%.2f)" % (B,H))
                        print("A = %.2f" % A)

        def CircleFormulas(userinput):

                PI = math.pi

                if userinput == 20: 
                        
                        L = float(input("What is the arc length?"))
                        x = float(input("What is the measure of the corresponding central angle?"))

                        XDiv = x / 360
                        FirstPar = L / XDiv
                        TwoPI = 2 * PI
                        r = FirstPar / TwoPI
                        rPI = r / PI
                        print("The radius of the circle is %.2f" %r)

                        print("Here is the process: ")
                        print("(L / X/360) / 2π = r")
                        print("(%.2f(%.2f/360)) / 2π = r" % (L,x))
                        print("(%.2f(%.2f)) / 2π = r" % (L,XDiv))
                        print("(%.2f / %.2f = r" % (FirstPar,TwoPI))
                        print("%.2f = r" %r)
                        print("In terms of π it is π%.2f" %rPI)
                        
                if userinput == 19: 

                       r = float(input("What is the radius of the circle?"))
                       L = float(input("What is the arc length of the given arc?"))
                       
                       TwoPI = 2 * PI
                       TwoPIr = TwoPI * r
                       FirstPar = L / TwoPIr
                       x = 360 * FirstPar
                       print("The measure of the corresponding central angle of the arc is %.2f degrees" %x)

                       print("Here is the process: ")
                       print("360(L / 2πr) = x")
                       print("360(%.2f / 2π%.2f = x" % (L,r))
                       print("360(%.2f / %.2f(%.2f)) = x" % (L,TwoPI,r))
                       print("360(%.2f /%.2f) = x" % (L,TwoPIr))
                       print("360(%.2f) = x" %FirstPar)
                       print("%.2f = x" %x)
                       
                if userinput == 18: 

                       r = float(input("What is the radius of the circle?"))
                       x = float(input("What is the measure of the central angle?"))

                       TwoPI = 2 * PI
                       TwoPIr = 2 * PI * r
                       XDiv = x / 360
                       L = TwoPIr * XDiv
                       LPI = L / PI
                       print("The length of the arc is %.2f" %L)

                       print("Here is the process: ")
                       print("L = 2πr(X/360)")
                       print("L = 2π(%.2f)(%.2f/360)" %(r,x))
                       print("L = %.2f(%.2f)(%.2f/360" %(TwoPI,r,x))
                       print("L = %.2f(%.2f)" %(TwoPIr,XDiv))
                       print("L = %.2f" %L)
                       print(" In terms of π it is π%.2f" %LPI)
                       
                if userinput == 17: 

                        SegmentArea = float(input("What is the area of the segment?"))
                        Radius = float(input("What is the radius of the circle?"))
                        Height = float(input("What is the height of the corresponding triangle?"))
                        CentAng = float(input("What is the measure of the corresponding arcs central angle?"))

                        CentAngDiv = CentAng / 360
                        RadiusSquared = Radius**2
                        PIRSQR = RadiusSquared * PI
                        FirstSec = CentAngDiv * PIRSQR
                        TwoFirstSec = SegmentArea - FirstSec
                        FirstSecTwo = 2 * TwoFirstSec
                        FirstParTwo = FirstSecTwo / Height
                        NegativeOne = 0 - 1
                        Base = FirstParTwo / NegativeOne
                        print("The measure of the corresponding triangles base is %.2f" % Base)

                        print("Here is the process: ")
                        print("(2(A - X/360(πr^2)) / h) / -1 = b")
                        print("(2(%.2f - %.2f/360(π%.2f^2)) / %.2f) / -1 = b" % (SegmentArea,CentAng,Radius,Height))
                        print("(2(%.2f - %.2f(π%.2f)) / %.2f) / -1 = b" % (SegmentArea,CentAngDiv,RadiusSquared,Height))
                        print("(2(%.2f - %.2f(%.2f)) / %.2f) / -1 = b" %(SegmentArea,CentAngDiv,PIRSQR,Height))
                        print("(2(%.2f - %.2f) / %.2f) / -1 = b" % (SegmentArea,FirstSec,Height))
                        print("(2(%.2f) / %.2f / -1 = b" % (TwoFirstSec,Height))
                        print("(%.2f / %.2f) / -1 = b" % (FirstSecTwo,Height))
                        print("%.2f / -1 = b" % FirstParTwo)
                        print("%.2f = b" %Base)

                if userinput == 16: 

                        SegmentArea = float(input("What is the area of the segment?" ))
                        CentAng = float(input("What is the measure of the corresponding arcs central angle?" ))
                        Radius = float(input("What is the radius of the circle?" ))
                        Base = float(input("What is the measure of the corresponding triangles base?" ))

                        CentAngDiv = CentAng / 360
                        RadiusSquared = Radius**2
                        NegativeBase = 0 - Base
                        PIRSQR = PI * RadiusSquared
                        FirstSec = CentAngDiv * PIRSQR
                        FirstPar = SegmentArea - FirstSec
                        TwoFirstPar = 2 * FirstPar
                        Height = TwoFirstPar / NegativeBase
                        print("The height of the triangle is %.2f" %Height)

                        print("Here is the process: ")
                        print("2(A - X/360(πr^2)) / -b = h")
                        print("2(%.2f - %.2f / 360(π%.2f^2)) - %.2f = h" % (SegmentArea, CentAng, Radius, Base))
                        print("2(%.2f - %.2f(π%.2f)) / -%.2f = h" % (SegmentArea,CentAngDiv,RadiusSquared,Base))
                        print("2(%.2f - %.2f(%.2f)) / - %.2f = h" % (SegmentArea,CentAngDiv,PIRSQR,NegativeBase))
                        print("2(%.2f - %.2f) / -%.2f = h" % (SegmentArea,FirstSec,NegativeBase))
                        print("2(%.2f) / -%.2f = h" % (FirstPar,NegativeBase))
                        print("%.2f / -%.2f = h" % (TwoFirstPar,NegativeBase))
                        print("%.2f = h" % Height)

                if userinput == 15:

                        SegmentArea = float(input("What is the area of the segment?" ))
                        CentAng = float(input("What is the measure of the corresponding arcs central angle?"))
                        Base = float(input("What is the measure of the base of the corresponding triangle?"))
                        Height = float(input("What is the measure of the height of the corresponding triangle?"))

                        ATim = SegmentArea * 360
                        PIX = PI * CentAng
                        FirstPar = ATim / PIX
                        BH = Base * Height
                        Triangle = 0.5 * BH
                        RootInput = FirstPar + Triangle
                        Radius = math.sqrt(RootInput)
                        RadiusPI = Radius / PI
                        print("The radius of the circle is %.2f" %Radius)
                        
                        print("Here is the process: ")
                        print("(360A / π(x)) + 1/2bh)^0.5 = r")
                        print("(360%.2f / π(%.2f))  + 1/2(%.2f)(%.2f))^0.5 = r" % (SegmentArea,CentAng,Base,Height))
                        print("(%.2f / %.2f) + 1/2(%.2f))^0.5 = r" % (ATim,PIX,BH))
                        print("(%.2f + %.2f)^0.5 = r" % (FirstPar,Triangle))
                        print("(%.2f)^0.5 = r" %RootInput)
                        print("%.2f = r" %Radius)
                        print("In terms of π it is π%.2f" %RadiusPI)
          
                if userinput == 14: 

                       SegmentArea = float(input("What is the area of the segment?"))
                       Radius = float(input("What is the radius of the circle?"))
                       Base = float(input("What is the base of the corresponding height of the segment?"))
                       Height = float(input("What is the height of the corresponding height of the segment?"))

                       AX = SegmentArea * 360
                       RadiusSquared = Radius**2
                       PIRadiusSquared = PI * RadiusSquared
                       BH = Base * Height
                       Triangle = 0.5 * BH
                       FirstPar = AX / PIRadiusSquared
                       mARC = FirstPar + Triangle
                       mARCPI = mARC / PI
                       print("The measure of the corresponding arcs central angle is %.2f" %mARC)

                       print("Here is the process: ")
                       print("(360A/πr^2) + 1/2bh = X")
                       print("(360%.2f/π%.2f^2) + 1/2(%.2f)(%.2f) = X" % (SegmentArea,Radius,Base,Height))
                       print("(%.2f/π%.2f) + 1/2(%.2f) = X" % (AX, RadiusSquared, BH))
                       print("(%.2f/%.2f) + %.2f = X" % (AX,PIRadiusSquared,Triangle))
                       print("%.2f + %.2f = X" % (FirstPar, Triangle))
                       print("%.2f° = X" %mARC)
                       print("In terms of π it is π%.2f°" %mARCPI)

                       
                if userinput == 13:

                        CentAng = float(input("What is the measure of the segments corresponding central angle?"))
                        Radius = float(input("What is the radius of the circle?"))
                        Base = float(input("What is the base of the corresponding triangle with the segment?"))
                        Height = float(input("What is the height of the corresponding triangle with the segment?"))

                        CentAngDiv = CentAng / 360
                        RadiusSquared = Radius**2
                        PIRadSqr = PI * RadiusSquared
                        BH = Base * Height
                        Triangle = 0.5 * BH
                        FirstPar = CentAngDiv * PIRadSqr
                        SegmentArea = FirstPar - Triangle
                        print("The area of the segment is %.2f" %SegmentArea)

                        print("Here is the process: ")
                        print("A = X/360(πr^2) - 1/2bh")
                        print("A = %.2f°/360(π%.2f^2) - 1/2(%.2f)(%.2f)" % (CentAng,Radius,Base,Height))
                        print("A = %.2f(π%.2f) - 1/2(%.2f)" % (CentAngDiv,RadiusSquared,BH))
                        print("A = %.2f(%.2f) - %.2f" % (FirstPar,PIRadSqr,Triangle))
                        print("A = %.2f" %SegmentArea)
                              
                if userinput == 12:

                        AreaOfAnnulus = float(input("What is the area of the annulus? "))
                        SmallRadius = float(input("What is the measure of the small radius?" ))

                        SmallRadiusSquared = SmallRadius**2
                        PITimSmallRadiusSquared = PI * SmallRadiusSquared
                        AreaPlusPITimesSmallRadiusSquared = PITimSmallRadiusSquared + AreaOfAnnulus
                        DivPI = AreaPlusPITimesSmallRadiusSquared / PI
                        SquareRoot = math.sqrt(DivPI)
                        BigRadiusPI = SquareRoot / PI
                        print("The measure of the big radius is %.2f" %SquareRoot)

                        print("Here is the process: ")
                        print(" [(A + πr^2) / π]^0.5) = R")
                        print(" [(%.2f + π%.2f) / π]^0.5) = R" % (AreaOfAnnulus, SmallRadius))
                        print(" [(%.2f + %.2f) / π)^0.5] = R" % (AreaOfAnnulus, SmallRadiusSquared))
                        print(" [(%.2f + %.2f) / π]^0.5) = R" % (AreaOfAnnulus, PITimSmallRadiusSquared))
                        print(" [(%.2f / π ]) = R" %AreaPlusPITimesSmallRadiusSquared)
                        print(" [(%.2f)^0.5] = R" %DivPI)
                        print(" [(%.2f]) = R" %SquareRoot)
                        print("In terms of π it is π%.2f" %BigRadiusPI)
                              
                if userinput == 11: 
                        
                        AreaOfAnnulus = float(input("What is the measure of the annulus?"))
                        BigRadius = float(input("What is the measure of the big radius?"))

                        NegativePI = 0 - PI
                        PIRsqr = PI * BigRadius**2
                        AMPIRsqr = AreaOfAnnulus - PIRsqr
                        SquareRootInput = AMPIRsqr / NegativePI
                        SmallRadius = math.sqrt(SquareRootInput)
                        SmallRadiusPI = SmallRadius / PI
                        print("The measure of the small radius is %.2f" %SmallRadius)

                        print("Here is the process: ")
                        print("[(A - πR^2) / -π]^0.5 = r")
                        print("[(%.2f - π%.2f^2 / -π]^0.5 = r" % (AreaOfAnnulus , BigRadius))
                        print("(%.2f / -π)^0.5 = r" %AMPIRsqr)
                        print("(%.2f)^0.5 = r" %SquareRootInput)
                        print("%.2f = r" %SmallRadius)
                        print("In terms of π it is π%.2f" %SmallRadiusPI)
                
                                                         
                if userinput == 10:
                            
                        SR = float(input("What is the small radius? "))
                        BR = float(input("What is the big radius?" ))
                        SRSQR = SR**2
                        BRSQR = BR**2

                        AAnnulus = BR**2 * PI - SR**2 * PI
                        AAPI = AAnnulus / PI
                        print("The area of the annulus is %.2f" %AAnnulus)
                        print("Here is the process: ")
                        print("A = πR^2 - πr^2")
                        print("A = π%.2f^2 - π%.2f ^2" % (BR , SR))
                        print("A = π%.2f - π%.2f" % (BRSQR , SRSQR))
                        print("A = %.2f" %AAnnulus)
                        print("In terms of π it is π%.2f" %AAPI)
                               
                if userinput == 9:
                        ASEC = float(input("In order to find the measure of the radius, we need the area of the sector: "))
                        mCent = float(input("We also need the measure of the corresponding central angle: "))
                        ACircSec = ASEC * 360
                        PIX = PI * mCent
                        ACDIVPI = ACircSec / PIX
                        RADSECTOR = ACDIVPI**0.5
                        print("The radius of the sector given the measure of the central angle and the area of the sector is %.2f" %RADSECTOR)
                                    
                if userinput == 8:

                        mASector = float(input("In order to find the measure of the arc, we need the area of the sector"))
                        mASecRad = float(input("We will also need the radius of the circle"))
                        AX = mASector * 360
                        Denom = PI * mASecRad**2
                        mASecRadSqr = mASecRad**2
                        mArcSector = AX / Denom
                        print("The measure of the arc based on the area and radius is %.2f" %mArcSector)

                        print("Here is the process: ")
                        print("(360A / πr^2 = mARC ")
                        print("(360%.2f / π%.2f^2) = mARC" % (mASector , mASecRad))
                        print("(%.2f / π%.2f) = mARC" % (AX , mASecRadSqr))
                        print("%.2f° = mARC" %mArcSector)
                               
                if userinput == 7:
                        
                        mARC = float(input("In order to perform this function, we need the measure of the central angle: "))
                        mR = float(input("We also need the radius of the circle." ))
                        mARCDiv360 = mARC / 360
                        PIxr = PI * mR**2
                        mASec = mARCDiv360 * PIxr
                        mRSquared = mR**2
                        ASectorPI = mASec / PI
                        print("The area of the sector is %.2f" %mASec)
                        print("Here is the process: ")
                        print("Asector = (X/360) * (πr^2)")
                        print("Asector = (%.2f°/360) * (π%.2f^2)" % (mARC , mR))
                        print("Asector = (%.2f) * (π%.2f)" % (mARCDiv360 , mRSquared))
                        print("Asector = %.2f" %mASec)
                        print("In terms of π it is π%.2f" %ASectorPI)
                        
                if userinput == 6:
                        
                        AreaOfCircle = float(input('In order to perform this function, we need the area of the circle: '))
                        RotC = math.sqrt(AreaOfCircle / PI)
                        CBoA = 2 * PI * RotC
                        ADivPI = AreaOfCircle / PI 
                        print("The circumfrence of the circle based on the area is %.2f" %CBoA)
                        print("Here is the process: ")
                        print("First given the area of the circle we got the radius.")
                        print("(A / π)^0.5 = r")
                        print("%.2f / π)^0.5 = r" %AreaOfCircle)
                        print("%.2f^0.5 = r" %ADivPI)
                        print("%.2f = r" %RotC)
                        print("Now that we have the radius, we can find the circumfrence.")
                        print("C = 2πr")
                        print("C = 2π%.2f" %RotC)
                        print("C = %.2f" %CBoA)
                                
                if userinput == 5:
                        CoCC2= float(input('In order to perform this function, we need the circumfrence, what is the circumfrence of the circle?' ))
                        CDenominator = 2 * PI
                        RoC = CoCC2 / CDenominator
                        RoCSquared = RoC**2
                        print("Now we have the radius which we can use to find the area")
                        AoCC2 = RoC**2 * PI
                        AreaPI = AoCC2 / PI
                        print("The area based on the circumfrence is %.2f" %AoCC2)

                        print("Here is the process: ")
                        print("First, given the circumfrence we got the radius.")
                        print("C / 2π = r")
                        print("%.2f / 2π = r" %CoCC2)
                        print("%.2f = r" %RoC)
                        print("Now that we have the radius we can find the area.")
                        print("A = πr^2")
                        print("A = π%.2f^2" %RoC)
                        print("A = π%.2f" %RoCSquared)
                        print("A = %.2f" %AoCC2)
                        print("In terms of pi it is π%.2f" %AreaPI)
                                
                if userinput == 4:
                        
                        CoC = float(input('What is the circumfrence of the circle?' ))
                        Denominator = 2 * PI
                        RBC = CoC / Denominator
                        AnswerPI = RBC / PI
                        print("The radius of the circle is %.2f" %RBC)
                        print("Here is the process: ")
                        print("%.2f = 2πr" %CoC)
                        print("%.2f / 2π = r" %CoC)
                        print("%.2f = r" %RBC )
                        print("In terms of π it is π%.2f" %AnswerPI)

                if userinput == 3:

                        AofC = float(input('What is the area of the cirle?' ))
                        Sqrt = AofC / PI
                        RBA =  Sqrt**0.5
                        AnswerPI = RBA / PI
                        print("The radius of the circle is %.2f" %RBA)

                        print("Here is the process: ")
                        print("First we found the area of the circle, with the given radius")
                        print(" (Area/PI)^0.5 = r")
                        print("(%.2f / π)^0.5 = r" %AofC)
                        print("%.2f^0.5 = r" %Sqrt)
                        print("%.2f = r" %RBA)
                        print("In terms of π it is π%.2f" %AnswerPI)
                            
                if userinput == 2:

                        r = float(input('What is the radius of the circle?' ))
                        Circumfrence = 2 * PI * r
                        print("The circumfrence is %.2f" %Circumfrence)
                        TermsOfPI = Circumfrence / PI

                        print("Here is the process: ")
                        print("C = 2πr")
                        print("C = 2π%.2f" %r)
                        print("C = %.2f" %Circumfrence)
                        print("In terms of π it is π%.2f" %TermsOfPI )
                         
                if userinput == 1:
                        r = float(input('What is the radius of the circle?' ))
                        Area = r ** 2 * PI
                        print("The area of the circle is %.2f " %Area)
                        rsquared = r**2
                        print("Here is the process: ")
                        print("A = πr^2")
                        print("A = π%.2f^2" %r)
                        print("A = π%.2f" %rsquared)
                        print("A = %.2f" %Area)
                        print("In terms of π it is π%.2f" %rsquared)
                        
        myListCircles = [
                      "1 - area",
                      "2 - circumfrence",
                      "3 - radius based on area",
                      "4 - radius based on circumfrence",
                      "5 - Area based on circumfrence",
                      "6 - Circumfrence based on area",
                      "7 - Area of sector",
                      "8 - Measure of arc in degrees given area of sector and radius",
                      "9 - Measure of radius given the area and the measure of the arc in degrees.",
                      "10 - Area of annulus",
                      "11 - Measure of small radius based on area of annulus and measure of big radius",
                      "12 - Measure of big radius based on area of annulus and measure of small radius",
                      "13 - Area of segment",
                      "14 - Measure of central angle based on area of segment, base,radius of circle, and height of corresponding triangle",
                      "15 - Measure of radius based on central angle, base and height of corresponding triangle",
                      "16 - Measure of height based on central angle, radius of circle, measure of central angle, and measure of base",
                      "17 - Measrue of base, based on measure of height, central angle, radius, and area of segment",
                      "18 - Arc length of a circle",
                      "19 - Measure of arcs corresponding central angle based on radius of circle and arc length",
                      "20 - Measure of radius based on arc length and measure of corresponding central angle"
                      ]

        myListPolygons =[     "1 - Rectangles",
                              "2 - Base of rectangle based on height and area of rectangle",
                              "3 - Height of rectangle based on base and area of rectnagle",
                              "4 - Area of triangle",
                              "5 - Base of triangle based on height and area",
                              "6 - Height of triangle based on area and base",
                              "7 - Area of a trapezoid",
                              "8 - Height of trapezoid, based on area, base one, and base two",
                              "9 - Measure of the second base, based on the height and the area of the trapezoid",
                              "10 - Measure of the first base, based on the height and the area of the trapezoid",
                              "11 - Area of a kite",
                              "12 - Area of the first diagonal based on the area of kite and measure of the second diagonal"
                        ]

                              
        myListSubjects = [

                           "1 - Circles",
                           "2 - Polygons"
                          ]

            
        for response in myListSubjects:
                print(response)   

        SubjectChoice = int(input("Chose a subject(Number based)." ))
           
        if SubjectChoice == 1:

                for response in myListCircles:
                        print(response)
                userinput = int(input('Pick a formula' ))
                CircleFormulas(userinput)    

        if SubjectChoice == 2:
                
                for response in myListPolygons:
                        print(response)
                userinput = int(input("Pick a formula" ))
                PolygonFormulas(userinput)

while loop == True:
        Loopback = input("Would you like to restart the program (Y/N)")
        print(Loopback)

        if Loopback =='Y':
                loop = True
                print(myListSubjects)

        else:
                loop = False
                sys.exit(0)

     

        

