---
name: llm-development
description: LLM and ML development best practices with LangChain and transformers. Use when building AI/ML applications.
---

# LLM & ML Development

## Frameworks
- **LLM**: LangChain, transformers
- **Data**: pandas, numpy
- **API**: FastAPI with Pydantic

## Configuration Management
- Use Hydra or YAML for experiment configs
- Keep configs version-controlled
- Separate dev/staging/prod configurations

Example config structure:
```
config/
  base.yaml
  models/
    gpt4.yaml
    claude.yaml
  experiments/
    baseline.yaml
```

## Data Pipeline
- Manage data versions with DVC
- Document data sources and transformations
- Use consistent data formats
- Validate data at pipeline boundaries

## Model Versioning
- Version models with Git LFS or model registry
- Track experiments with MLflow or similar
- Log hyperparameters and metrics
- Save reproducibility info (seeds, versions)

## LangChain Best Practices
- Use LCEL (LangChain Expression Language) for chains
- Implement proper error handling for LLM calls
- Add retry logic for API failures
- Cache expensive operations

Example:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Summarize: {text}")
chain = prompt | llm | StrOutputParser()
```

## Prompt Engineering
- Store prompts as separate files or constants
- Version control prompt templates
- Test prompts with diverse inputs
- Document expected outputs

## Error Handling
- Catch and log LLM API errors
- Implement graceful degradation
- Set appropriate timeouts
- Handle rate limiting

## Performance
- Use async for I/O-bound LLM calls
- Implement caching for repeated queries
- Batch requests when possible
- Monitor token usage and costs

## Testing LLM Applications
- Mock LLM responses for unit tests
- Create integration tests with real calls
- Test edge cases and failure modes
- Validate output format and structure
