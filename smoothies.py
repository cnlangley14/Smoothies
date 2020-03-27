#!/usr/bin/env python3
from app import app
from app.smoothie import Smoothie, mysmoothies


def main():
    ms = Smoothie("Matt's smoothie")
    ms.add_ingredient("apples")
    ms.add_ingredient("milk")
    ms.add_ingredient("carrots")
    ms.add_ingredient("kale")
    ms.add_steps("wash fruit")
    ms.add_steps("add ingredients")
    ms.add_steps("blend smoothie")
    mysmoothies.append(ms)


    cs = Smoothie("Chereese's Smoothie")
    cs.add_ingredient("peanut butter")
    cs.add_ingredient("almond milk")
    cs.add_ingredient("whey protein")
    cs.add_ingredient("6 ice cubes")
    cs.add_ingredient("4 frozen bananas")
    cs.add_steps("add almond milk")
    cs.add_steps("add rest of the ingredients")
    cs.add_steps("give the excess PB to Baxter")
    cs.add_steps("blend drink")
    mysmoothies.append(cs)
    app.run(host="0.0.0.0")


    


if __name__ == "__main__":
    main()