[Lectures](https://www.youtube.com/playlist?list=PLujxSBD-JXgnGmsn7gEyN28P1DnRZG7qi)

# Light transport algorithms

## Radiometry

The measured 'quantity' in a light transport simulation is *radiance*. It is a measure of
the amount of energy ('radiant flux') over a unit area, for a unit angle. In other words,

```math
\mathtt{Radiance:} \quad L [W / (m^2 \cdot sr)]
```

However, we cannot do a true electromagnetic radiation simulation, using Maxwells equations,
as nanometer scale simulations are not viable.

Instead, the 'rendering equation' can be used to approximate it.

## Intersection notation

From a point of contact $`x`$, several vectors are defined:

- $`\vec V`$: direction towards the camera

- $`\vec R`$: reflected ray at angle $`\theta_i`$

- $`\vec N`$: surface normal

- $`\vec L`$: direction towards light source

## Reflective materials

- Specular materials reflect incoming rays perfectly around the surface normal

- Diffuse materials reflect incoming rays towards a random point on a unit sphere placed
  with its base on the contact point

- Glossy materials are in-between, reflecting incoming rays in a random 'oval' shape
  biased towards the direction of a specular reflection.

### BRDF

The bidirectional reflectance distribution function takes an incoming ray, a contact point,
and an outgoing ray, and gives the probability that the final output ray is the provided ray.

```math
f_r (\vec\omega, x, \vec\omega')
```
