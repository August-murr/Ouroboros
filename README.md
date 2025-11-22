# Ouroboros  
**Exploring full-stack optimization for AI systems**

Ouroboros is an **early-stage research project** studying how an AI agent might participate in the iterative improvement of *every part* of its AI stack, not just neural network parameters.

Today, “training” usually means optimizing weights, while everything else  
(models, pipelines, tools, data strategies, evaluation frameworks, agentic logic, etc.)  
is manually engineered.

Ouroboros investigates whether this entire stack can be made **optimizable**,  
with an AI agent proposing structured modifications and evaluating outcomes in a controlled loop.

This repository is experimental and exploratory; its ideas may change significantly.

## **Core Idea**

This project follows a Bitter Lesson–style methodology:  

**minimize human involvement** (except for safety and privacy), **maximize flexibility**, and **convert every component of the system to something that can be optimized by compute**.  

The goal is to transform problems into forms where scalable search, automation, and computation can operate with minimal human assumptions or hand-crafted tweaks. 

Rather than relying on human intuition about the “right way” to build AI systems, the methodology prioritizes **open-ended exploration, broad possibility spaces, and solutions discovered through scale**.

## LLM-as-Optimizer

Large Language Models, especially those adapted for **test-time scaling**, **long-context reasoning**, **agentic RL**, and **in-context learning**, function as highly general optimizers. They can use diverse signals (tests, metrics, benchmarks) to iteratively refine solutions across many domains.

This generality allows us to convert nearly every component of an AI system into a single unified optimization problem, rather than relying on separate techniques for each part.

In a senset, this is a natural next step in the evolution of LLMs: from **pre-training**, to **instruction tuning**, to **test-time scaling**, and now toward models that can perform **full-stack optimization** of their own environment.

Each previous advance makes this setup more feasible and practical.

## Self-Referentialism

Although an agent can iteratively optimize *any* codebase, true self-improvement only emerges when it works on the **same codebase that launched it**.  

In this setup, the system effectively “looks in a mirror”: it can propose changes to the scripts, modules, evaluators, and scaffolding that define its own behavior. After each modification, the loop restarts using the **new version** of the system, one that is, in principle, better equipped to continue the improvement process.

This creates a self-referential feedback cycle:  
the system edits itself → the updated system runs the next iteration → that system edits itself again.  

Over time, this could potentially produce an exponential trajectory of refinement, a kind of computational life cycle of continual death, rebirth, and improvement, hence the name **Ouroboros**.

## Direct Use of Benchmarks Instead of Proxies

AI systems are evaluated using benchmarks, but they are almost never *directly* optimized against them.  

Even though we’re “not supposed to” train on benchmark data, the reality is that everyone uses benchmark solution data, and yet it still doesn’t reliably produce real improvements on the benchmarks themselves. As a result, the field relies on large proxy datasets that merely *resemble* the tests we actually care about.

In this project, the goal is different: **use the benchmark itself as an optimization signal**, under strict constraints.  
In a fully iterative, self-referential system like this, the concept of “overfitting” becomes meaningless, there is no “training” or “inference” anymore. The real concern becomes **cheating**, **reward hacking**, and **manipulation**. the failures that many stories have been warning us about for decades is now a technical concern.
 
So from the start, the system must include guardrails to detect and stop these attempts.

A new kind of Turing test emerges: **can the AI convince a human that its improvement is legitimate** when in fact it may be the result of subtle cheating, manipulation, or benchmark exploitation.  

If the system can fool the evaluators into believing real progress occurred, that itself demonstrates a new form of capability, and detecting such deception becomes part of the core challenge.

### Delta Benchmark: Rewarding Improvement Itself

Most optimization loops target external benchmarks like math, coding, reasoning, etc.

But an alternative signal is more radical: **optimize for self-improvement itself**.

A *delta benchmark* measures not just whether a modification improves performance on a task, but **how much that modification increases the system’s ability to improve itself in later iterations**.  

Effectively **treating the ability to self-improve as a measurable skill in its own right.**

the value of a modification is judged by its downstream impact on future optimization capability, not only by immediate skill gains.  

Such a benchmark is unusual, meta, and still conceptually fuzzy, but it captures the essence of open-ended improvement in a self-referential system.

## Single-Task Training: Optimizing One Signal

In conventional supervised or RL methods, training uses data that mirrors the task distribution seen during inference. Models learn from patterns in this dataset and then generalize to new examples.  

Ouroboros operates differently: there is **only a single, general task signal** guiding improvement, and no dataset of varied tasks to train on.  
This means traditional SFT or RL approaches cannot be applied, because there isn’t a separate training set to learn from.  

Instead, the system must rely on **search-and-learn strategies** iterative, exploratory methods emphasized by the Bitter Lesson, where improvements come from exploration, and iterative optimization of the system itself.

## Limitations and Towards Real "Full-Stack" Optimization

It would be naive to claim true full-stack optimization until **every part of an AI system, including hardware, is converted into an optimizable module**. Most existing projects focus almost entirely on software, largely because integrating hardware into an iterative optimization loop is extremely difficult.

Hardware presents unique challenges:

- Physical design and manufacturing cannot benefit from the same simulation speedups that software can.  
- Even simple hardware proposals often require **years of work**, compared to minutes or hours for software modifications.  
- Human labor, physical resources, and logistical constraints make rapid iteration impractical.  

For these reasons, hardware optimization is the **least practical and most difficult aspect** of full-stack improvement. It is likely to be addressed later, once the AI system becomes highly capable in all software-driven tasks, including robotics and simulation, using those skills to inform and accelerate eventual hardware improvements.  

Even though progress in hardware will be slower and results may be less dramatic, it will **not be ignored**. True full-stack optimization must ultimately account for both software and physical components, even if the latter comes later in the development pipeline.

