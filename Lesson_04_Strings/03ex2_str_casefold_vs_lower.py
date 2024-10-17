"""Casefold vs lowercase example."""
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

text = 'ß is a German letter'

# Using casefold() method
casefolded_text = text.casefold()
logger.info(f'Casefolded text: {casefolded_text}')

# Using lower() method
lowercased_text = text.lower()
logger.info(f'Lowercased text: {lowercased_text}')

# Comparing the results
if casefolded_text == lowercased_text:
    logger.info('casefold() and lower() produce the same result.')
else:
    logger.info('casefold() and lower() produce different results.')
