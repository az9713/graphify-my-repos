---
repo: deepagents_langchain
description: Clone of langchain-ai deepagents for cli study
language: Python
stars: 0
forks: 0
created: 2025-11-04
updated: 2025-11-08
topics: 
is_fork: False
kb: 442
---

# deepagents_langchain
# 🧠🤖 Deep Agents

Build powerful AI agents that can plan, use tools, and solve complex tasks.

## What is This?

**DeepAgents** is a Python library for building AI agents that go beyond simple chatbots. These agents can:

- 📋 **Plan** multi-step tasks
- 🔧 **Use tools** to interact with the world
- 📁 **Remember** information using files
- 🤝 **Delegate** work to specialized sub-agents
- 🔍 **Monitor** their own performance
- ⚡ **Cache** results for speed
- 🔬 **Analyze** code structure
- ⏱️ **Execute** tasks in parallel

## ⭐ What's New in This Repository

This enhanced version includes **5 powerful new features** (developed with Claude Code assistance):

1. **Observability Middleware** - Track execution, tool calls, and token usage
2. **Smart Caching** - Speed up operations and reduce AI costs
3. **Code Analysis** - Analyze Python code structure with AST
4. **Parallel Execution** - Run multiple tasks concurrently
5. **Evaluation Framework** - Test and benchmark agent performance

> **Note:** This repository demonstrates the capabilities of AI-assisted development. All features, documentation, and examples were implemented with [Claude Code](https://claude.ai/code) assistance, showcasing how AI agents can build complex software systems.

## 🚀 Quick Start

**New to AI agents?** Start here:

1. **[Getting Started Guide](GETTING_STARTED.md)** - Complete beginner's tutorial
2. **[Installation Guide](INSTALLATION.md)** - Step-by-step setup for Windows/Mac/Linux
3. **[Core Concepts](CONCEPTS.md)** - Understand how agents work
4. **[Tutorials](TUTORIALS.md)** - 8 hands-on tutorials

**Already familiar with agents?** Jump to:

- **[API Reference](API_REFERENCE.md)** - Complete API documentation
- **[Examples Directory](examples/)** - Working code examples
- **[Feature Documentation](#new-features)** - Details on the 5 new features

## 📚 Documentation

| Document | Description | Audience |
|----------|-------------|----------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Your first agent in 5 minutes | Beginners |
| [INSTALLATION.md](INSTALLATION.md) | Platform-specific installation | Everyone |
| [CONCEPTS.md](CONCEPTS.md) | How agents, tools, and middleware work | Beginners |
| [TUTORIALS.md](TUTORIALS.md) | Step-by-step tutorials | Beginners |
| [API_REFERENCE.md](API_REFERENCE.md) | Complete API documentation | Developers |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common problems and solutions | Everyone |

## Prerequisites

**You need:**
- Python 3.11 or higher
- Basic Python knowledge
- An Anthropic API key ([get one free](https://console.anthropic.com/))

**You DON'T need:**
- Prior AI/ML experience
- Knowledge of LangChain
- Advanced Python skills

## Simple Example

Here's a complete agent in just a few lines:

```python
from langchain_core.tools import tool
from deepagents import create_deep_agent

# Define a tool the agent can use
@tool
def calculator(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# Create the agent
agent = create_deep_agent(
    tools=[calculator],
    system_prompt="You are a helpful math assistant."
)

# Use it!
result = agent.invoke({
    "messages": [{"role": "user", "content": "What is 25 + 17?"}]
})

print(result["messages"][-1].content)
# Output: "The answer is 42"
```

**That's it!** The agent:
1. Reads your question
2. Decides to use the calculator tool
3. Calls `calculator(25, 17)`
4. Returns the answer

## About Deep Agents

Using an LLM to call tools in a loop is the simplest form of an agent.
This architecture, however, can yield agents that are "shallow" and fail to plan and act over longer, more complex tasks.

Applications like "Deep Research", "Manus", and "Claude Code" have gotten around this limitation by implementing a combination of four things:
a **planning tool**, **sub agents**, access to a **file system**, and a **detailed prompt**.

<img src="deep_agents.png" alt="deep agent" width="600"/>

`deepagents` is a Python package that implements these in a general purpose way so that you can easily create a Deep Agent for your application.

**Acknowledgements: This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.**

## Installation

### Quick Install

```bash
# Clone this repository
git clone https://github.com/az9713/deepagents_langchain.git
cd deepagents_langchain

# Install
pip install -e .

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"
```

### Detailed Installation

For platform-specific instructions (Windows/Mac/Linux), virtual environments, and troubleshooting, see:

👉 **[Complete Installation Guide](INSTALLATION.md)**

## Usage

(To run the example below, you will need to `pip install tavily-python`).

Make sure to set `TAVILY_API_KEY` in your environment. You can generate one [here](https://www.tavily.com/).

```python
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Web search tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research, and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

# Create the deep agent
agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions,
)

# Invoke the agent
result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})
```

See [examples/research/research_agent.py](examples/research/research_agent.py) for a more complex example.

The agent created with `create_deep_agent` is just a LangGraph graph - so you can interact with it (streaming, human-in-the-loop, memory, studio)
in the same way you would any LangGraph agent.

## Core Capabilities
**Planning & Task Decomposition**

 Deep Agents include a built-in `write_todos` tool that enables agents to break down complex tasks into discrete steps, track progress, and adapt plans as new information emerges.

**Context Management**

 File system tools (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`) allow agents to offload large context to memory, preventing context window overflow and enabling work with variable-length tool results.

**Subagent Spawning**

 A built-in `task` tool enables agents to spawn specialized subagents for context isolation. This keeps the main agent’s context clean while still going deep on specific subtasks.

**Long-term Memory**

 Extend agents with persistent memory across threads using LangGraph’s Store. Agents can save and retrieve information from previous conversations.

## Customizing Deep Agents

There are several parameters you can pass to `create_deep_agent` to create your own custom deep agent.

### `model`

By default, `deepagents` uses `"claude-sonnet-4-5-20250929"`. You can customize this by passing any [LangChain model object](https://python.langchain.com/docs/integrations/chat/).

```python
from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent

model = init_chat_model("openai:gpt-4o")
agent = create_deep_agent(
    model=model,
)
```

### `system_prompt`
Deep Agents come with a built-in system prompt. This is relatively detailed prompt that is heavily based on and inspired by [attempts](https://github.com/kn1026/cc/blob/main/claudecode.md) to [replicate](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-code.md)
Claude Code's system prompt. It was made more general purpose than Claude Code's system prompt. The default prompt contains detailed instructions for how to use the built-in planning tool, file system tools, and sub agents.

Each deep agent tailored to a use case should include a custom system prompt specific to that use case as well. The importance of prompting for creating a successful deep agent cannot be overstated.

```python
from deepagents import create_deep_agent

research_instructions = """You are an expert researcher. Your job is to conduct thorough research, and then write a polished report.
"""

agent = create_deep_agent(
    system_prompt=research_instructions,
)
```

### `tools`

Just like with tool-calling agents, you can provide a deep agent with a set of tools that it has access to.

```python
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

agent = create_deep_agent(
    tools=[internet_search]
)
```

### `middleware`
`create_deep_agent` is implemented with middleware that can be customized. You can provide additional middleware to extend functionality, add tools, or implement custom hooks. 

```python
from langchain_core.tools import tool
from deepagents import create_deep_agent
from langchain.agents.middleware import AgentMiddleware

@tool
def get_weather(city: str) -> str:
    """Get the weather in a city."""
    return f"The weather in {city} is sunny."

@tool
def get_temperature(city: str) -> str:
    """Get the temperature in a city."""
    return f"The temperature in {city} is 70 degrees Fahrenheit."

class WeatherMiddleware(AgentMiddleware):
  tools = [get_weather, get_temperature]

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-20250514",
    middleware=[WeatherMiddleware()]
)
```

#### ObservabilityMiddleware

The `ObservabilityMiddleware` provides comprehensive telemetry and monitoring for your agents:

```python
from deepagents import create_deep_agent, ObservabilityMiddleware

# Console monitoring (great for development)
agent = create_deep_agent(
    tools=[my_tool],
    middleware=[
        ObservabilityMiddleware(
            export_mode="console",
            console_verbose=True
        )
    ]
)

# File export (for analysis)
agent = create_deep_agent(
    tools=[my_tool],
    middleware=[
        ObservabilityMiddleware(
            export_mode="file",
            export_file_path="/logs/telemetry.json"
        )
    ]
)

# Custom callback (for production monitoring)
def send_to_monitoring(event):
    # Send to your monitoring system
    print(f"Event: {event.event_type}")

agent = create_deep_agent(
    tools=[my_tool],
    middleware=[
        ObservabilityMiddleware(
            export_mode="callback",
            on_event_callback=send_to_monitoring
        )
    ]
)

# Access metrics programmatically
obs = ObservabilityMiddleware(export_mode="none")
agent = create_deep_agent(middleware=[obs])

# Run your agent...
agent.invoke({"messages": [{"role": "user", "content": "..."}]})

# Get summary
summary = obs.get_summary()
print(f"Total tokens: {summary['total_tokens']}")
print(f"Tool calls: {summary['tool_calls']}")
```

**Key Features:**
- **Token Usage Tracking**: Monitor LLM costs and optimize prompts
- **Tool Call Analytics**: Track timing and success rates for all tools
- **Execution Tracing**: See the complete flow of agent operations
- **Flexible Export**: Console, file, or custom callbacks for integration with monitoring platforms

See [examples/observability/](examples/observability/) for detailed examples.

#### CachingMiddleware

The `CachingMiddleware` provides intelligent caching to reduce costs and improve performance:

```python
from deepagents import create_deep_agent, CachingMiddleware

# In-memory caching (fast, non-persistent)
agent = create_deep_agent(
    tools=[expensive_tool],
    middleware=[
        CachingMiddleware(
            backend="memory",
            ttl=3600  # 1 hour
        )
    ]
)

# File-based caching (persistent across restarts)
agent = create_deep_agent(
    tools=[api_tool],
    middleware=[
        CachingMiddleware(
            backend="/tmp/agent_cache.json",
            ttl=3600
        )
    ]
)

# Selective caching (cache specific tools only)
agent = create_deep_agent(
    tools=[fast_tool, slow_tool, api_tool],
    middleware=[
        CachingMiddleware(
            backend="memory",
            cache_tools=["slow_tool", "api_tool"],  # Only cache these
            ttl=3600
        )
    ]
)

# Access cache statistics
caching_mw = CachingMiddleware(backend="memory")
agent = create_deep_agent(middleware=[caching_mw])

# After running...
stats = caching_mw.get_stats()
print(f"Cache hits: {stats['hits']}, Hit rate: {stats['hit_rate']:.1%}")

# Clear cache or invalidate specific entries
caching_mw.clear_cache()
caching_mw.invalidate("tool_name", {"arg": "value"})
```

**Key Features:**
- **Cost Reduction**: Cache expensive API calls and tool results
- **Performance**: Dramatically faster for repeated operations
- **Multiple Backends**: In-memory (fast) or file-based (persistent)
- **TTL Support**: Automatic expiration with configurable time-to-live
- **Selective Caching**: Choose which tools to cache
- **Cache Management**: Statistics, clearing, and invalidation

See [examples/caching/](examples/caching/) for detailed examples.

#### CodeAnalysisMiddleware

The `CodeAnalysisMiddleware` provides powerful code analysis capabilities using AST parsing:

```python
from deepagents import create_deep_agent, CodeAnalysisMiddleware

# Enable code analysis tools
agent = create_deep_agent(
    system_prompt="You are a code review expert",
    middleware=[
        CodeAnalysisMiddleware(
            languages=["python"],
            enable_ast_analysis=True
        )
    ]
)

# Use the tools
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "Analyze mycode.py and find all function definitions"
    }]
})
```

**Available Tools:**
- `find_functions(file_path)` - Find all function definitions with args and docstrings
- `find_classes(file_path)` - Find all class definitions with methods and bases
- `find_imports(file_path)` - Find all import statements
- `analyze_file_structure(file_path)` - Get high-level code structure overview

**Key Features:**
- **AST-Based Analysis**: Parse Python code structure accurately
- **Function Discovery**: Find all functions with signatures and documentation
- **Class Analysis**: Discover classes, methods, and inheritance
- **Import Tracking**: Identify all dependencies
- **Structure Overview**: Get counts and summaries of code elements

See [examples/code_analysis/](examples/code_analysis/) for detailed examples.

#### ParallelExecutionMiddleware

The `ParallelExecutionMiddleware` enables agents to execute multiple tasks concurrently with dependency management:

```python
from deepagents import create_deep_agent, ParallelExecutionMiddleware

# Enable parallel task execution
agent = create_deep_agent(
    tools=[fetch_weather, fetch_news, fetch_stock],
    middleware=[
        ParallelExecutionMiddleware(max_workers=5)
    ]
)

# Use the parallel_task tool
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": """Use parallel_task to fetch:
        1. Weather for San Francisco
        2. News about technology
        3. Stock price for AAPL
        """
    }]
})
```

**Available Tool:**
- `parallel_task(tasks)` - Execute multiple tasks in parallel with optional dependencies

**Key Features:**
- **Parallel Execution**: Run independent tasks simultaneously for faster results
- **Dependency Management**: Define task dependencies with `depends_on` field
- **Result Aggregation**: Automatically collect and merge results from all tasks
- **Error Handling**: Continue execution even if some tasks fail
- **Concurrency Control**: Limit maximum parallel workers with `max_workers`
- **Performance Tracking**: Track execution duration for each task

**Example with dependencies:**
```python
# Tasks 1 and 2 run in parallel, task 3 waits for both
parallel_task(tasks=[
    {"task_id": "task1", "tool_name": "calculate_sum", "tool_args": {"a": 10, "b": 5}},
    {"task_id": "task2", "tool_name": "calculate_sum", "tool_args": {"a": 8, "b": 3}},
    {"task_id": "task3", "tool_name": "multiply", "tool_args": {"a": 15, "b": 11},
     "depends_on": ["task1", "task2"]}
])
```

See [examples/parallel_execution/](examples/parallel_execution/) for detailed examples.

## Evaluation Framework

The DeepAgents Evaluation Framework provides comprehensive tools for testing and benchmarking agent performance.

### AgentEvaluator

Test your agents with custom test cases, pre-built benchmarks, and custom metrics:

```python
from deepagents import create_deep_agent
from deepagents.evaluation import AgentEvaluator, Benchmark, contains_metric

agent = create_deep_agent(tools=[my_tool])

# Define test cases
test_cases = [
    {
        "name": "test_1",
        "input": {"messages": [{"role": "user", "content": "Calculate 2+2"}]},
        "expected": "4"
    }
]

# Run evaluation
evaluator = AgentEvaluator(
    agent=agent,
    test_cases=test_cases,
    metrics={"accuracy": contains_metric}
)

report = evaluator.run()
print(f"Pass rate: {report.get_pass_rate():.1f}%")
```

### Pre-Built Benchmarks

Evaluate agents against standard capability benchmarks:

```python
from deepagents.evaluation import Benchmark, BenchmarkType

# Get specific benchmark
reasoning_tests = Benchmark.get_benchmark_by_type(BenchmarkType.REASONING)

# Run evaluation
evaluator = AgentEvaluator(
    agent=agent,
    test_cases=reasoning_tests,
    metrics={"contains": contains_metric}
)

report = evaluator.run()
```

**Available Benchmarks:**
- `PLANNING` - Task breakdown and prioritization
- `TOOL_USE` - Tool invocation and error handling
- `REASONING` - Logical deduction and problem solving
- `MEMORY` - Context retention and recall
- `RESEARCH` - Information finding and synthesis

### A/B Testing

Compare two agents on the same test cases:

```python
agent_a = create_deep_agent(model="anthropic:claude-sonnet-4-20250514")
agent_b = create_deep_agent(model="anthropic:claude-haiku-3-5-20250514")

evaluator = AgentEvaluator(
    agent=agent_a,
    test_cases=test_cases,
    metrics={"accuracy": contains_metric}
)

results = evaluator.compare_agents(agent_b, agent_names=("Sonnet", "Haiku"))

print(f"Sonnet: {results['Sonnet'].get_pass_rate():.1f}%")
print(f"Haiku: {results['Haiku'].get_pass_rate():.1f}%")
```

### Custom Metrics

Define domain-specific evaluation criteria:

```python
from deepagents.evaluation import (
    exact_match_metric,
    contains_metric,
    keyword_presence_metric,
    length_metric,
    numeric_accuracy_metric
)

def custom_metric(output, expected):
    """Check if output meets custom criteria."""
    return 1.0 if meets_criteria(output) else 0.0

evaluator = AgentEvaluator(
    agent=agent,
    test_cases=test_cases,
    metrics={
        "exact_match": exact_match_metric,
        "contains": contains_metric,
        "custom": custom_metric
    }
)
```

### Saving Reports

Export evaluation results to JSON:

```python
report = evaluator.run()
evaluator.save_report(report, "evaluation_report.json")
```

**Key Features:**
- **Custom Test Cases**: Define your own t