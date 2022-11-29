<article class="day-desc">
 <h2>
  --- Day 1: The Tyranny of the Rocket Equation ---
 </h2>
 <p>
  Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him
  <span title="If only you had time to grab an astrolabe.">
   measurements
  </span>
  from
  <em class="star">
   fifty stars
  </em>
  .
 </p>
 <p>
  Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants
  <em class="star">
   one star
  </em>
  . Good luck!
 </p>
 <p>
  The Elves quickly load you into a spacecraft and prepare to launch.
 </p>
 <p>
  At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.  They haven't determined the amount of fuel required yet.
 </p>
 <p>
  Fuel required to launch a given
  <em>
   module
  </em>
  is based on its
  <em>
   mass
  </em>
  .  Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
 </p>
 <p>
  For example:
 </p>
 <ul>
  <li>
   For a mass of
   <code>
    12
   </code>
   , divide by 3 and round down to get
   <code>
    4
   </code>
   , then subtract 2 to get
   <code>
    2
   </code>
   .
  </li>
  <li>
   For a mass of
   <code>
    14
   </code>
   , dividing by 3 and rounding down still yields
   <code>
    4
   </code>
   , so the fuel required is also
   <code>
    2
   </code>
   .
  </li>
  <li>
   For a mass of
   <code>
    1969
   </code>
   , the fuel required is
   <code>
    654
   </code>
   .
  </li>
  <li>
   For a mass of
   <code>
    100756
   </code>
   , the fuel required is
   <code>
    33583
   </code>
   .
  </li>
 </ul>
 <p>
  The Fuel Counter-Upper needs to know the total fuel requirement.  To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
 </p>
 <p>
  <em>
   What is the sum of the fuel requirements
  </em>
  for all of the modules on your spacecraft?
 </p>
</article>

### --- Part Two ---

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

- A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
- At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
- The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
  <br>
  What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
