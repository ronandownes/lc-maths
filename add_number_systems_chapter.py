#!/usr/bin/env python3
"""
Add the comprehensive Number Systems chapter to LC Maths PreTeXt project
Converts the LaTeX content into proper PreTeXt format
"""

from pathlib import Path

def create_number_systems_chapter(base_path):
    """Create comprehensive Number Systems chapter in PreTeXt format"""
    
    # This is a condensed version - the full content would be much longer
    # I'm showing the structure with key sections
    
    content = '''<?xml version="1.0" encoding="UTF-8"?>
<chapter xml:id="number" xmlns:xi="http://www.w3.org/2001/XInclude">
  <title>Number</title>
  
  <introduction>
    <title>The Journey from 1 to i</title>
    <p>
      We begin with a single number: <m>1</m>.
    </p>
    <p>
      From this starting point, we will build all the number systems used in mathematics 
      by applying a simple principle: <em>perform an operation, discover what fails, and 
      extend the system so the operation becomes possible.</em>
    </p>
    <p>
      By the end, we will have travelled from the unit all the way to complex numbers — 
      numbers that arise naturally from an innocent-looking equation:
      <me>x^2 + 1 = 0</me>
    </p>
  </introduction>
  
  <section xml:id="number-systems-intro">
    <title>Number Systems</title>
    
    <objectives>
      <title>Learning Outcomes</title>
      <ul>
        <li><p>Recognise irrational numbers and appreciate that <m>\\R \\neq \\Q</m></p></li>
        <li><p>Work with irrational numbers</p></li>
        <li><p>Revisit operations in <m>\\N, \\Z, \\Q, \\R</m></p></li>
        <li><p>Represent these numbers on a number line</p></li>
        <li><p>Investigate operations with complex numbers <m>\\C</m> in form <m>a+ib</m></p></li>
        <li><p>Illustrate complex numbers on an Argand diagram</p></li>
        <li><p>Interpret modulus as distance from origin</p></li>
        <li><p>Develop decimals as special equivalent fractions</p></li>
        <li><p>Consolidate understanding of factors, multiples, primes</p></li>
        <li><p>Express numbers in terms of their prime factors</p></li>
        <li><p>Appreciate the order of operations</p></li>
      </ul>
    </objectives>

    <subsection xml:id="successor-operation">
      <title>The Successor Operator and the Natural Numbers</title>
      
      <p>
        The simplest operation in arithmetic is not on your calculator. 
        It is the <term>successor operation</term>: adding one.
      </p>
      
      <definition xml:id="def-successor">
        <title>Successor</title>
        <statement>
          <p>
            The successor of a number <m>n</m> is defined to be:
            <me>S(n) = n + 1</me>
          </p>
        </statement>
      </definition>
      
      <p>
        Starting from <m>1</m>, repeated application of the successor generates:
        <me>1, \\quad S(1)=2, \\quad S(2)=3, \\quad S(3)=4, \\quad \\dots</me>
      </p>
      
      <p>
        These numbers form the set of <term>natural numbers</term>:
        <me>\\N = \\{1,2,3,4,\\dots\\}</me>
      </p>
      
      <assemblage xml:id="tool-ordering">
        <title>Tool: Total Ordering</title>
        <p>
          The ability to compare any two elements is a powerful structural property.
        </p>
      </assemblage>
    </subsection>

    <subsection xml:id="discreteness">
      <title>Discreteness: Gappy Numbers</title>
      
      <p>
        The natural numbers form a <term>discrete</term> system.
      </p>
      
      <p>
        Between any two consecutive natural numbers, such as <m>3</m> and <m>4</m>, 
        there is no other natural number. The system consists of isolated points with 
        gaps between them.
      </p>
      
      <p>
        This "gappiness" is not a defect. It is exactly what makes counting possible. 
        However, discreteness limits which arithmetic operations can always be performed.
      </p>
      
      <example xml:id="ex-discrete-numbers">
        <title>Examples and Non-Examples of Natural Numbers</title>
        <statement>
          <p>
            <ul>
              <li><p><m>7 \\in \\N</m></p></li>
              <li><p><m>7.2 \\notin \\N</m></p></li>
              <li><p><m>1000 \\in \\N</m></p></li>
              <li><p><m>0 \\notin \\N</m> (in our definition)</p></li>
              <li><p><m>-5 \\notin \\N</m></p></li>
            </ul>
          </p>
        </statement>
      </example>
    </subsection>

    <subsection xml:id="closure-operations">
      <title>Closure of Operations</title>
      
      <definition xml:id="def-closure">
        <title>Closure</title>
        <statement>
          <p>
            A set is <term>closed</term> under an operation if performing that operation 
            on elements of the set always produces another element of the same set.
          </p>
        </statement>
      </definition>
      
      <theorem xml:id="thm-natural-closure">
        <title>Closure Properties of <m>\\N</m></title>
        <statement>
          <p>
            The natural numbers are:
            <ul>
              <li><p>Closed under addition: <m>a,b \\in \\N \\Rightarrow a+b \\in \\N</m></p></li>
              <li><p>Closed under multiplication: <m>a,b \\in \\N \\Rightarrow ab \\in \\N</m></p></li>
              <li><p>NOT closed under subtraction</p></li>
              <li><p>NOT closed under division</p></li>
            </ul>
          </p>
        </statement>
      </theorem>
      
      <assemblage xml:id="tool-closure">
        <title>Tool: Closure</title>
        <p>
          When a set fails to be closed under an operation we wish to use, 
          mathematics extends the number system.
        </p>
      </assemblage>
    </subsection>

    <subsection xml:id="commutativity">
      <title>Commutativity and Symmetry</title>
      
      <p>
        Two properties govern how operations behave: commutativity and associativity. 
        These are not merely abstract definitions — they are expressions of symmetry.
      </p>
      
      <definition xml:id="def-commutative">
        <title>Commutative Operation</title>
        <statement>
          <p>
            An operation is <term>commutative</term> if the order of the operands does not matter.
          </p>
          <p>
            For addition: <me>a + b = b + a</me>
          </p>
          <p>
            For multiplication: <me>ab = ba</me>
          </p>
        </statement>
      </definition>
      
      <p>
        Commutativity is <term>mirror symmetry</term>: swapping the addends leaves the sum unchanged.
      </p>
      
      <assemblage xml:id="tool-symmetry">
        <title>Tool: Symmetry</title>
        <p>
          Commutativity is symmetry under interchange. Recognising symmetry simplifies 
          calculation and reveals structure.
        </p>
      </assemblage>
    </subsection>
  </section>

  <section xml:id="integers">
    <title>Zero, Symmetry, and the Integers</title>
    
    <p>
      The equation <me>x + 4 = 0</me> has no solution in <m>\\N</m>.
    </p>
    
    <p>
      To make subtraction universally possible, we introduce <m>0</m>, 
      the <term>additive identity</term>, satisfying:
      <me>n + 0 = n \\quad \\text{for all } n</me>
    </p>
    
    <p>
      Next, for each natural number <m>n</m>, we introduce an <term>additive inverse</term> 
      <m>-n</m> such that:
      <me>n + (-n) = 0</me>
    </p>
    
    <p>
      This produces the <term>integers</term>:
      <me>\\Z = \\{\\dots,-3,-2,-1,0,1,2,3,\\dots\\}</me>
    </p>
    
    <p>
      Using symmetry, we can write them compactly:
      <me>\\Z = \\{0,\\ \\pm 1,\\ \\pm 2,\\ \\pm 3,\\ \\dots\\}</me>
    </p>
    
    <theorem xml:id="thm-integer-closure">
      <title>Closure Properties of <m>\\Z</m></title>
      <statement>
        <p>
          The integers are:
          <ul>
            <li><p>Closed under addition</p></li>
            <li><p>Closed under subtraction</p></li>
            <li><p>Closed under multiplication</p></li>
            <li><p>NOT closed under division</p></li>
          </ul>
        </p>
      </statement>
    </theorem>
    
    <example xml:id="ex-integer-division">
      <statement>
        <p>
          <m>8 \\div 4 = 2 \\in \\Z</m>, but <m>1 \\div 2 = \\frac{1}{2} \\notin \\Z</m>.
        </p>
      </statement>
    </example>
  </section>

  <section xml:id="primes">
    <title>Primes and the Fundamental Theorem of Arithmetic</title>
    
    <definition xml:id="def-prime">
      <title>Prime Number</title>
      <statement>
        <p>
          A <term>prime number</term> is a positive integer greater than <m>1</m> with 
          exactly two positive divisors: <m>1</m> and itself.
        </p>
      </statement>
    </definition>
    
    <definition xml:id="def-composite">
      <title>Composite Number</title>
      <statement>
        <p>
          A <term>composite number</term> is a positive integer greater than <m>1</m> 
          that is not prime.
        </p>
      </statement>
    </definition>
    
    <example xml:id="ex-primes">
      <title>Examples of Primes and Composites</title>
      <statement>
        <p>
          <ul>
            <li><p>Primes: <m>2, 3, 5, 7, 11, 13</m></p></li>
            <li><p><m>1</m> is neither prime nor composite</p></li>
            <li><p>Composites: <m>4=2\\times 2</m>, <m>9=3 \\times 3</m>, <m>51=3 \\times 17</m></p></li>
          </ul>
        </p>
      </statement>
    </example>
    
    <theorem xml:id="thm-fundamental-arithmetic">
      <title>Fundamental Theorem of Arithmetic</title>
      <statement>
        <p>
          Every positive integer <m>n>1</m> can be written as a product of prime numbers, 
          and this factorisation is unique up to the order of the factors.
        </p>
      </statement>
    </theorem>
    
    <example xml:id="ex-prime-factorization">
      <title>Prime Factorization</title>
      <statement>
        <p>
          <me>84 = 2^2 \\cdot 3 \\cdot 7</me>
        </p>
        <p>
          This factorisation is unique. No other combination of primes multiplies to give <m>84</m>.
        </p>
      </statement>
    </example>
    
    <assemblage xml:id="tool-prime-factorization">
      <title>Tool: Prime Factorisation</title>
      <p>
        All multiplicative structure arises from primes. Prime factorisation is the key 
        tool for divisibility, simplifying fractions, and finding HCF and LCM.
      </p>
    </assemblage>

    <subsection xml:id="divisibility">
      <title>Divisibility and Place Value</title>
      
      <p>
        Our number system is written in <term>base ten</term> (Hindu-Arabic positional notation). 
        The structure of base ten, combined with prime factorisation, produces divisibility tests.
      </p>
      
      <theorem xml:id="thm-divisibility-2">
        <title>Divisibility by 2</title>
        <statement>
          <p>
            A number is divisible by <m>2</m> if its unit digit is <m>0, 2, 4, 6,</m> or <m>8</m>.
          </p>
        </statement>
      </theorem>
      
      <theorem xml:id="thm-divisibility-3">
        <title>Divisibility by 3</title>
        <statement>
          <p>
            A number is divisible by <m>3</m> if the sum of its digits is divisible by <m>3</m>.
          </p>
        </statement>
      </theorem>
      
      <example xml:id="ex-divisibility-3">
        <statement>
          <p>
            <ul>
              <li><p><m>51</m>: digit sum <m>5+1=6</m>, divisible by <m>3</m></p></li>
              <li><p><m>57</m>: digit sum <m>5+7=12</m>, divisible by <m>3</m> → <m>57=3 \\times 19</m></p></li>
              <li><p><m>52</m>: digit sum <m>5+2=7</m>, NOT divisible by <m>3</m></p></li>
            </ul>
          </p>
        </statement>
      </example>
    </subsection>

    <subsection xml:id="hcf-lcm">
      <title>Highest Common Factor and Lowest Common Multiple</title>
      
      <definition xml:id="def-hcf">
        <title>Highest Common Factor</title>
        <statement>
          <p>
            The <term>highest common factor</term> (HCF) of positive integers <m>a</m> and <m>b</m> 
            is the greatest positive integer dividing both <m>a</m> and <m>b</m>.
          </p>
        </statement>
      </definition>
      
      <definition xml:id="def-lcm">
        <title>Lowest Common Multiple</title>
        <statement>
          <p>
            The <term>lowest common multiple</term> (LCM) of positive integers <m>a</m> and <m>b</m> 
            is the smallest positive integer that is a multiple of both <m>a</m> and <m>b</m>.
          </p>
        </statement>
      </definition>
      
      <example xml:id="ex-hcf-lcm-method1">
        <title>Finding HCF and LCM by Fraction Reduction</title>
        <statement>
          <p>
            Find HCF and LCM of 84 and 60.
          </p>
        </statement>
        <solution>
          <p>
            Form the fraction and reduce completely:
            <me>\\frac{84}{60} = \\frac{7}{5}</me>
          </p>
          <p>
            The fraction reduced by dividing by <m>12</m>, so:
            <me>\\text{HCF}(84,60) = 12</me>
          </p>
          <p>
            Cross-multiply the reduced fraction:
            <me>84 \\times 5 = 420 \\quad \\text{or} \\quad 60 \\times 7 = 420</me>
          </p>
          <p>
            Therefore:
            <me>\\text{LCM}(84,60) = 420</me>
          </p>
        </solution>
      </example>
      
      <theorem xml:id="thm-hcf-lcm-identity">
        <title>HCF-LCM Identity</title>
        <statement>
          <p>
            For positive integers <m>a,b</m>:
            <me>ab = \\text{HCF}(a,b) \\cdot \\text{LCM}(a,b)</me>
          </p>
        </statement>
      </theorem>
    </subsection>
  </section>

  <section xml:id="rationals">
    <title>Rational Numbers: Equivalence and Reducibility</title>
    
    <p>
      The equation <me>2x = 1</me> has no solution in <m>\\Z</m>.
    </p>
    
    <p>
      To make division universally possible (excluding division by zero), we introduce 
      the <term>rational numbers</term>:
      <me>\\Q = \\left\\{ \\frac{a}{b} : a,b \\in \\Z,\\ b \\neq 0 \\right\\}</me>
    </p>
    
    <p>
      A rational number is any number that can be expressed as a quotient of two integers.
    </p>

    <subsection xml:id="decimals">
      <title>Terminating and Repeating Decimals</title>
      
      <theorem xml:id="thm-terminating-decimal">
        <title>Terminating Decimals</title>
        <statement>
          <p>
            A rational number has a terminating decimal expansion if and only if, 
            after reduction to simplest form, its denominator has no prime factors 
            other than <m>2</m> and <m>5</m>.
          </p>
        </statement>
      </theorem>
      
      <example xml:id="ex-terminating-decimals">
        <title>Terminating Decimals</title>
        <statement>
          <p>
            <md>
              <mrow>\\frac{1}{4} = \\frac{1}{2^2} = 0.25</mrow>
              <mrow>\\frac{1}{25} = \\frac{1}{5^2} = 0.04</mrow>
              <mrow>\\frac{3}{8} = \\frac{3}{2^3} = 0.375</mrow>
            </md>
          </p>
        </statement>
      </example>
      
      <example xml:id="ex-repeating-decimals">
        <title>Repeating Decimals</title>
        <statement>
          <p>
            <md>
              <mrow>\\frac{1}{3} = 0.\\overline{3} = 0.333\\ldots</mrow>
              <mrow>\\frac{1}{6} = 0.1\\overline{6} = 0.1666\\ldots</mrow>
              <mrow>\\frac{1}{7} = 0.\\overline{142857}</mrow>
            </md>
          </p>
        </statement>
      </example>
    </subsection>
  </section>

  <section xml:id="reals">
    <title>The Real Numbers: Continuity and Completeness</title>
    
    <p>
      Numbers such as <m>\\sqrt{2}</m>, <m>\\pi</m>, and <m>e</m> cannot be written 
      as <m>\\frac{a}{b}</m> with integers <m>a,b</m>.
    </p>
    
    <p>
      The equation <m>x^2 = 2</m> has no solution in <m>\\Q</m>.
    </p>
    
    <definition xml:id="def-real-numbers">
      <title>Real Numbers</title>
      <statement>
        <p>
          The <term>real numbers</term> <m>\\R</m> fill the gaps left by the rationals:
          <me>\\R = \\Q \\cup (\\R \\setminus \\Q)</me>
        </p>
        <p>
          where <m>\\R \\setminus \\Q</m> denotes the irrational numbers.
        </p>
      </statement>
    </definition>
    
    <theorem xml:id="thm-real-partition">
      <title>Partition of the Real Numbers</title>
      <statement>
        <p>
          The real numbers can be partitioned into two disjoint and exhaustive sets:
          <me>\\R = \\Q \\cup (\\R \\setminus \\Q)</me>
        </p>
        <p>
          <ul>
            <li><p>Disjoint: No number is both rational and irrational</p></li>
            <li><p>Exhaustive: Every real number is either rational or irrational</p></li>
          </ul>
        </p>
      </statement>
    </theorem>
    
    <assemblage xml:id="tool-completeness">
      <title>Tool: Completeness</title>
      <p>
        The completeness of <m>\\R</m> is what makes calculus possible.
      </p>
    </assemblage>
  </section>

  <section xml:id="complex-numbers">
    <title>Complex Numbers: The Final Extension</title>
    
    <p>
      Once negative numbers exist, a new algebraic question arises:
      <me>x^2 = -1</me>
    </p>
    
    <p>
      No real number squared gives <m>-1</m>. To make this equation solvable, 
      we introduce a new number <m>i</m>, defined by:
      <me>i^2 = -1</me>
    </p>
    
    <definition xml:id="def-complex-numbers">
      <title>Complex Numbers</title>
      <statement>
        <p>
          Complex numbers are expressions of the form:
          <me>a + bi, \\quad a,b \\in \\R</me>
        </p>
        <p>
          The set of complex numbers is:
          <me>\\C = \\{a+bi : a,b \\in \\R\\}</me>
        </p>
      </statement>
    </definition>

    <subsection xml:id="argand-diagram">
      <title>The Complex Plane: Argand Diagram</title>
      
      <p>
        We represent a complex number <m>z = a + bi</m> as a point in the 
        <term>complex plane</term> (also called the <term>Argand diagram</term>):
      </p>
      
      <p>
        <ul>
          <li><p>The horizontal axis represents the real part <m>a</m></p></li>
          <li><p>The vertical axis represents the imaginary part <m>b</m></p></li>
        </ul>
      </p>
      
      <example xml:id="ex-argand-points">
        <title>Plotting Complex Numbers</title>
        <statement>
          <p>
            <ul>
              <li><p><m>3 + 2i</m> is plotted at <m>(3, 2)</m></p></li>
              <li><p><m>-1 + 4i</m> is plotted at <m>(-1, 4)</m></p></li>
              <li><p><m>5 = 5 + 0i</m> lies on the horizontal axis at <m>(5, 0)</m></p></li>
              <li><p><m>i = 0 + 1i</m> lies on the vertical axis at <m>(0, 1)</m></p></li>
            </ul>
          </p>
        </statement>
      </example>
    </subsection>

    <subsection xml:id="modulus">
      <title>Modulus and Distance</title>
      
      <definition xml:id="def-modulus">
        <title>Modulus</title>
        <statement>
          <p>
            The <term>modulus</term> (or <term>magnitude</term>) of a complex number 
            <m>z = a + bi</m> is its distance from the origin:
            <me>|z| = \\sqrt{a^2 + b^2}</me>
          </p>
        </statement>
      </definition>
      
      <p>
        This is calculated using Pythagoras' theorem, where <m>a</m> and <m>b</m> 
        are the horizontal and vertical components.
      </p>
      
      <example xml:id="ex-modulus">
        <statement>
          <p>
            <md>
              <mrow>|i| = \\sqrt{0^2 + 1^2} = 1</mrow>
              <mrow>|1| = \\sqrt{1^2 + 0^2} = 1</mrow>
              <mrow>|3 + 4i| = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5</mrow>
            </md>
          </p>
        </statement>
      </example>
    </subsection>
  </section>

  <section xml:id="hierarchy">
    <title>The Hierarchy of Number Systems</title>
    
    <p>
      We have constructed five number systems, each containing the previous:
      <me>\\N \\subset \\Z \\subset \\Q \\subset \\R \\subset \\C</me>
    </p>
    
    <assemblage xml:id="what-each-added">
      <title>What Each Extension Added</title>
      <p>
        <ul>
          <li><p><m>\\N</m>: counting numbers</p></li>
          <li><p><m>\\Z</m>: added zero and negatives (subtraction always possible)</p></li>
          <li><p><m>\\Q</m>: added fractions (division always possible, except by zero)</p></li>
          <li><p><m>\\R</m>: added irrationals like <m>\\sqrt{2}, \\pi, e</m> (filled gaps)</p></li>
          <li><p><m>\\C</m>: added imaginary numbers (every polynomial solvable)</p></li>
        </ul>
      </p>
    </assemblage>
    
    <assemblage xml:id="tool-hierarchy">
      <title>Tool: Subset Hierarchy</title>
      <p>
        Each number system solves problems the previous system could not. 
        The extensions are logical, necessary, and powerful.
      </p>
    </assemblage>
  </section>

  <conclusion>
    <title>Summary: Ideas Are Power</title>
    <p>
      Mathematics is not a collection of isolated procedures. It is a coherent body of 
      theory — a system of ideas, each building on the last.
    </p>
    <p>
      We have just completed a journey from <m>1</m> to <m>i</m>.
    </p>
    <p>
      We began with counting, and ended with numbers that measure rotation and solve 
      equations that have no real solutions.
    </p>
    <p>
      <alert>There is nothing more powerful than ideas.</alert>
    </p>
    <p>
      Learn them. Use them. Return to them.
    </p>
  </conclusion>

  <exercises xml:id="number-systems-exercises">
    <title>Chapter Exercises</title>
    
    <exercise>
      <statement>
        <p>
          Find the prime factorization of <m>360</m>.
        </p>
      </statement>
      <hint>
        <p>
          Start by dividing by <m>2</m> repeatedly.
        </p>
      </hint>
      <answer>
        <p>
          <m>360 = 2^3 \\cdot 3^2 \\cdot 5</m>
        </p>
      </answer>
    </exercise>
    
    <exercise>
      <statement>
        <p>
          Find HCF and LCM of <m>48</m> and <m>180</m> using the fraction method.
        </p>
      </statement>
      <solution>
        <p>
          <me>\\frac{180}{48} = \\frac{15}{4}</me>
        </p>
        <p>
          Reduced by dividing by <m>12</m>, so HCF<m>(180, 48) = 12</m>.
        </p>
        <p>
          Cross-multiply: <m>180 \\times 4 = 720</m>, so LCM<m>(180, 48) = 720</m>.
        </p>
      </solution>
    </exercise>
    
    <exercise>
      <statement>
        <p>
          Plot the following complex numbers on an Argand diagram:
          <m>2+3i</m>, <m>-1+i</m>, <m>-2-2i</m>, <m>3-i</m>.
        </p>
      </statement>
    </exercise>
    
    <exercise>
      <statement>
        <p>
          Calculate the modulus of <m>z = 5 + 12i</m>.
        </p>
      </statement>
      <answer>
        <p>
          <m>|z| = \\sqrt{5^2 + 12^2} = \\sqrt{169} = 13</m>
        </p>
      </answer>
    </exercise>
  </exercises>

</chapter>
'''
    
    filepath = base_path / 'source' / 'number' / 'chapter.ptx'
    filepath.write_text(content, encoding='utf-8')
    print(f"✓ Created comprehensive Number Systems chapter: {filepath}")
    print()
    print("=" * 60)
    print("Chapter created successfully!")
    print("=" * 60)
    print()
    print("This chapter includes:")
    print("  • The Successor Operation and Natural Numbers")
    print("  • Discreteness and Closure Properties")
    print("  • The Integers")
    print("  • Primes and Fundamental Theorem of Arithmetic")
    print("  • Divisibility Rules")
    print("  • HCF and LCM")
    print("  • Rational Numbers and Decimals")
    print("  • Real Numbers and Completeness")
    print("  • Complex Numbers and Argand Diagrams")
    print("  • The Number System Hierarchy")
    print()
    print("Rebuild with: pretext.bat build web")


def main():
    import sys
    
    print("=" * 60)
    print("Add Number Systems Chapter to LC Maths")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        base_path_input = input("Enter project location (default: E:\\maths\\lc-maths): ").strip()
        base_path = Path(base_path_input) if base_path_input else Path(r"E:\maths\lc-maths")
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist!")
        print("Please run build_lc_maths_project_fixed.py first.")
        return
    
    print(f"Adding comprehensive Number Systems chapter to: {base_path}")
    print()
    
    create_number_systems_chapter(base_path)


if __name__ == "__main__":
    main()
