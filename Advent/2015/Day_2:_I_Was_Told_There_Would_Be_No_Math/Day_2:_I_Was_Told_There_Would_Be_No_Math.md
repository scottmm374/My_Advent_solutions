<article class="day-desc">
 <h2>
  --- Day 2: I Was Told There Would Be No Math ---
 </h2>
 <p>
  The elves are running low on wrapping paper, and so they need to submit an order for more.  They have a list of the dimensions (length
  <code>
   l
  </code>
  , width
  <code>
   w
  </code>
  , and height
  <code>
   h
  </code>
  ) of each present, and only want to order exactly as much as they need.
 </p>
 <p>
  Fortunately, every present is a box (a perfect
  <a href="https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid">
   right rectangular prism
  </a>
  ), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is
  <code>
   2*l*w + 2*w*h + 2*h*l
  </code>
  .  The elves also need a little extra paper for each present: the area of the smallest side.
 </p>
 <p>
  For example:
 </p>
 <ul>
  <li>
   A present with dimensions
   <code>
    2x3x4
   </code>
   requires
   <code>
    2*6 + 2*12 + 2*8 = 52
   </code>
   square feet of wrapping paper plus
   <code>
    6
   </code>
   square feet of slack, for a total of
   <code>
    58
   </code>
   square feet.
  </li>
  <li>
   A present with dimensions
   <code>
    1x1x10
   </code>
   requires
   <code>
    2*1 + 2*10 + 2*10 = 42
   </code>
   square feet of wrapping paper plus
   <code>
    1
   </code>
   square foot of slack, for a total of
   <code>
    43
   </code>
   square feet.
  </li>
 </ul>
 <p>
  All numbers in the elves' list are in
  <span title="Yes, I realize most of these presents are luxury yachts.">
   feet
  </span>
  .  How many total
  <em>
   square feet of wrapping paper
  </em>
  should they order?
 </p>
</article>


## PART 2

--- Part Two ---
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
