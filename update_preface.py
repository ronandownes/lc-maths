#!/usr/bin/env python3
"""
Update the LC Maths preface with comprehensive "How to Use This Book" content
"""

from pathlib import Path

def update_preface(base_path):
    """Update main.ptx with comprehensive preface"""
    
    content = '''<?xml version="1.0" encoding="UTF-8"?>
<pretext xmlns:xi="http://www.w3.org/2001/XInclude">
  
  <docinfo>
    <macros>
      \\newcommand{\\N}{\\mathbb{N}}
      \\newcommand{\\Z}{\\mathbb{Z}}
      \\newcommand{\\Q}{\\mathbb{Q}}
      \\newcommand{\\R}{\\mathbb{R}}
      \\newcommand{\\C}{\\mathbb{C}}
    </macros>
    
    <latex-image-preamble>
      \\usepackage{tikz}
      \\usepackage{pgfplots}
      \\pgfplotsset{compat=1.18}
    </latex-image-preamble>
  </docinfo>

  <book xml:id="lc-maths-ol">
    <title>Leaving Certificate Mathematics</title>
    <subtitle>Ordinary Level</subtitle>

    <frontmatter xml:id="frontmatter">
      <titlepage>
        <author>
          <personname>Mr Ronan Downes</personname>
        </author>
        <date><today/></date>
      </titlepage>

      <preface xml:id="preface">
        <title>How to Use This Book</title>
        
        <subsection xml:id="course-overview">
          <title>The Leaving Certificate Mathematics Course: Complete Overview</title>
          
          <p>
            The Leaving Certificate Mathematics course consists of <alert>five strands</alert>:
          </p>
          
          <ol>
            <li>
              <p>
                <alert>Statistics and Probability</alert> <mdash/> Counting, Probability, 
                Random Processes and Outcomes, Statistical Reasoning, Defining/Collecting/Organizing 
                Data, Representing Data, and Inference.
              </p>
            </li>
            <li>
              <p>
                <alert>Geometry and Trigonometry</alert> <mdash/> Synthetic Geometry, 
                Coordinate Geometry, Trigonometry, and Transformations.
              </p>
            </li>
            <li>
              <p>
                <alert>Number</alert> <mdash/> Number Systems, Indices and Standard Form, 
                Arithmetic and Proportion, and Mensuration (Length, Area, and Volume).
              </p>
            </li>
            <li>
              <p>
                <alert>Algebra</alert> <mdash/> Expressions, Equations, Inequalities, 
                and Complex Numbers.
              </p>
            </li>
            <li>
              <p>
                <alert>Functions</alert> <mdash/> Functions and Calculus.
              </p>
            </li>
          </ol>
          
          <p>
            That is the entire course.
          </p>
        </subsection>

        <subsection xml:id="five-proficiencies">
          <title>The Five Mathematical Proficiencies</title>
          
          <p>
            Success in mathematics depends on a rich combination of understanding, technique, 
            reasoning, and attitude. Research identifies <alert>five interrelated proficiencies</alert>:
          </p>
          
          <ul>
            <li>
              <p>
                <alert>Conceptual understanding</alert> <mdash/> comprehension of mathematical 
                concepts, operations, and relationships;
              </p>
            </li>
            <li>
              <p>
                <alert>Procedural fluency</alert> <mdash/> skill in carrying out procedures 
                flexibly, accurately, efficiently, and appropriately;
              </p>
            </li>
            <li>
              <p>
                <alert>Strategic competence</alert> <mdash/> ability to formulate, represent, 
                and solve mathematical problems;
              </p>
            </li>
            <li>
              <p>
                <alert>Adaptive reasoning</alert> <mdash/> capacity for logical thought, 
                reflection, explanation, and justification;
              </p>
            </li>
            <li>
              <p>
                <alert>Productive disposition</alert> <mdash/> habitual inclination to see 
                mathematics as sensible, useful, and worthwhile, coupled with belief in 
                diligence and one's own efficacy.
              </p>
            </li>
          </ul>
          
          <p>
            These proficiencies do not develop from reading alone. But the big ideas of 
            mathematics can <em>only</em> be appreciated through careful study of dense 
            theoretical exposition.
          </p>
        </subsection>

        <subsection xml:id="exam-structure">
          <title>The Exam Structure and Your Preparation</title>
          
          <p>
            The Leaving Certificate Mathematics paper has two sections, each worth 50%:
          </p>
          
          <ul>
            <li>
              <p>
                <alert>Section A: Concepts and Skills</alert> <mdash/> testing understanding 
                of core ideas and execution of standard procedures.
              </p>
            </li>
            <li>
              <p>
                <alert>Section B: Contexts and Applications</alert> <mdash/> testing 
                problem-solving, mathematical reasoning, and work in unfamiliar contexts.
              </p>
            </li>
          </ul>
          
          <p>
            To prepare effectively:
          </p>
          
          <ul>
            <li>
              <p>
                <alert>Study the theory</alert> (this book) for conceptual understanding.
              </p>
            </li>
            <li>
              <p>
                <alert>Work exercises</alert> to develop procedural fluency for Section A.
              </p>
            </li>
            <li>
              <p>
                <alert>Tackle problem sheets</alert> to build strategic competence for Section B.
              </p>
            </li>
          </ul>
          
          <p>
            The problem sheets provide scaffolded access to exam-level questions by using 
            smaller numbers and fewer steps initially, then gradually increasing complexity. 
            By the end, you will recognize patterns and think: <q>This is what I do now.</q>
          </p>
        </subsection>

        <subsection xml:id="how-to-use">
          <title>How to Use This Book</title>
          
          <p>
            There are no summary boxes. No bullet-point lists of <q>what to remember.</q> 
            No exercises embedded in the text.
          </p>
          
          <p>
            <alert>Everything here is a summary.</alert>
          </p>
          
          <p>
            This exposition is dense, direct, and to the point. To over-explain is to hide 
            the beauty of mathematics. The entire course is presented in comprehensive 
            theoretical chapters.
          </p>
          
          <p>
            <alert>Your job:</alert> Read it. Read it again. Write it out. Learn it.
          </p>
        </subsection>

        <subsection xml:id="book-structure">
          <title>Book Structure</title>
          
          <p>
            This book is organized by the five curriculum strands. Each strand contains 
            the complete theory you need:
          </p>
          
          <dl width="narrow">
            <li>
              <title>Statistics and Probability</title>
              <p>
                Counting, probability concepts, random processes, statistical reasoning, 
                data collection and representation, inference and hypothesis testing.
              </p>
            </li>
            <li>
              <title>Geometry and Trigonometry</title>
              <p>
                Synthetic geometry (theorems and constructions), coordinate geometry, 
                trigonometry (including sine and cosine rules), transformations and enlargements.
              </p>
            </li>
            <li>
              <title>Number</title>
              <p>
                Number systems (from <m>\\N</m> to <m>\\C</m>), primes and divisibility, 
                sequences and indices, arithmetic and proportion, mensuration.
              </p>
            </li>
            <li>
              <title>Algebra</title>
              <p>
                Expressions (expanding, factorizing, simplifying), equations (linear, 
                quadratic, simultaneous), inequalities.
              </p>
            </li>
            <li>
              <title>Functions</title>
              <p>
                Function concepts, graphing, composite functions, limits, differentiation, 
                maxima and minima, curve sketching.
              </p>
            </li>
          </dl>
        </subsection>

        <subsection xml:id="study-approach">
          <title>Your Study Approach</title>
          
          <p>
            <alert>This is not a textbook to skim.</alert>
          </p>
          
          <p>
            Each chapter presents mathematical ideas in their logical order. The concepts 
            build on each other. You cannot skip ahead without missing essential foundations.
          </p>
          
          <p>
            Study systematically:
          </p>
          
          <ol>
            <li><p>Read each section carefully with pen and paper at hand</p></li>
            <li><p>Write out definitions, theorems, and examples yourself</p></li>
            <li><p>Work through the reasoning step by step</p></li>
            <li><p>Return to difficult sections multiple times</p></li>
            <li><p>Practice exercises to develop fluency</p></li>
            <li><p>Tackle problem sheets to build strategic competence</p></li>
          </ol>
          
          <p>
            Mathematics is learned by doing, not by passive reading.
          </p>
        </subsection>

        <subsection xml:id="final-note">
          <title>A Final Note</title>
          
          <p>
            Your exam is in June. Time is limited.
          </p>
          
          <p>
            This book gives you the theory. Exercises and problem sheets give you the practice.
          </p>
          
          <p>
            Together, they provide everything you need to excel in Leaving Certificate Mathematics.
          </p>
          
          <p>
            <alert>There is nothing more powerful than ideas.</alert>
          </p>
          
          <p>
            Learn them. Use them. Return to them.
          </p>
          
          <p>
            Trust the process. You will be more than prepared.
          </p>
        </subsection>
      </preface>
    </frontmatter>

    <!-- Include chapter files -->
    <xi:include href="stats-probability/chapter.ptx"/>
    <xi:include href="geometry-trig/chapter.ptx"/>
    <xi:include href="number/chapter.ptx"/>
    <xi:include href="algebra/chapter.ptx"/>
    <xi:include href="functions/chapter.ptx"/>

    <backmatter xml:id="backmatter">
      <index>
        <title>Index</title>
        <index-list/>
      </index>
    </backmatter>

  </book>
</pretext>
'''
    
    filepath = base_path / 'source' / 'main.ptx'
    filepath.write_text(content, encoding='utf-8')
    print(f"✓ Updated {filepath}")
    print()
    print("=" * 60)
    print("Preface updated successfully!")
    print("=" * 60)
    print()
    print("The preface now includes:")
    print("  • Complete course overview (5 strands)")
    print("  • The five mathematical proficiencies")
    print("  • Exam structure (Section A & B)")
    print("  • How to prepare effectively")
    print("  • How to use this book")
    print("  • Book structure")
    print("  • Your study approach")
    print("  • Final motivational note")
    print()
    print("Rebuild with:")
    print("  cd E:\\maths\\lc-maths")
    print("  pretext.bat build web")
    print("  pretext.bat view web")


def main():
    import sys
    
    print("=" * 60)
    print("Update LC Maths Preface")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        base_path_input = input("Enter project location (default: E:\\maths\\lc-maths): ").strip()
        base_path = Path(base_path_input) if base_path_input else Path(r"E:\maths\lc-maths")
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist!")
        return
    
    print(f"Updating preface in: {base_path}")
    print()
    
    update_preface(base_path)


if __name__ == "__main__":
    main()
