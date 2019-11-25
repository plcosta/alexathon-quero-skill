# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# =========================
INSTALLMENTS_ANSWERS = [
  'Encontrei 2 mensalidades em aberto, do mês corrente e do mês passado.',
  'Encontrei 1 mensalidade em atraso com vencimento dia 10.',
]

CLASS_CONFIRMATION_ANSWERS = [
  'Você não tem aula de biologia hoje, elas são terças e quintas!',
  'Hoje você tem duas aulas de biologia no primeiro horário!',
  'Sim, hoje terá aula de biologia'
]

PERFORMANCE_ANSWERS = [
  'A nota mais recente do André em biologia foi 7 no dia quinze de outubro'
]

CALENDAR_ANSWERS = [
  'A próxima prova será de matemática no dia 25 de novembro.',
  'Ele tem uma prova de matemática amanhã! Ele deve está estudando!'
]

CHILD_CLASS_ANSWERS = [
  'O André tirou 7 em biologia na ultima prova!',
  'A ultima nota do André em biologia foi 9!',
  'O André ainda não realizou a prova de biologia'
]

CHILD_CALENDAR_ANSWERS = [
  'A próxima prova do André é amanhã!',
  'O André tem prova no dia 27 de novembro!',
  'O André tem uma prova marcada para semana que vem'
]
# =========================


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Olá, no Quero Pago você pode consultar suas mensalidades, calendário acadêmico e a performance nos seus cursos."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


# class HelloWorldIntentHandler(AbstractRequestHandler):
#     """Handler for Hello World Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "Olá mundo! Eu mando um Oi pra qual cidade?"
#         reprompt_output = "Manda um oi pra Fortaleza"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 .ask(reprompt_output)
#                 .response
#         )

# class CaptureHelloCityIntentHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("CaptureHelloCityIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "Olá mundo! Eu mando um Oi pra qual cidade?"
#         reprompt_output = "Manda um oi pra Fortaleza"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 # .ask(reprompt_output)
#                 .response
#         )

class InstallmentsIntentHandler(AbstractRequestHandler):
    """Handler for Installments Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("InstallmentsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(INSTALLMENTS_ANSWERS)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(reprompt_output)
                .response
        )

class WhastappIntentHandler(AbstractRequestHandler):
    """Handler for Installments Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhastappIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "O boleto em pdf foi enviado para o seu whatsapp"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(reprompt_output)
                .response
        )

class CalendarIntentHandler(AbstractRequestHandler):
    """Handler for Installments Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CalendarIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(CALENDAR_ANSWERS)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(reprompt_output)
                .response
        )

class ClassConfirmationIntentHandler(AbstractRequestHandler):
    """Handler for Installments Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ClassConfirmationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # slots = handler_input.request_envelope.request.intent.slots
        # disciplina = slots["disciplina"].value
        # speak_output = random.choice(CLASS_CONFIRMATION_ANSWERS).format(disciplina=disciplina)
        speak_output = random.choice(CLASS_CONFIRMATION_ANSWERS)
        # reprompt_output = "Desculpe, você precisa confirmar a disciplina."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(reprompt_output)
                .response
        )

class StatementIntentHandler(AbstractRequestHandler):
    """Handler for Installments Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StatementIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(PERFORMANCE_ANSWERS)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(reprompt_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Desculpe, não entendi. Como posso te ajudar?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class YesIntentHandler(AbstractRequestHandler):
    """Handler for Yes Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NoIntentHandler(AbstractRequestHandler):
    """Handler for No Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Tchau!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
# sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(InstallmentsIntentHandler())
sb.add_request_handler(WhastappIntentHandler())
sb.add_request_handler(StatementIntentHandler())
sb.add_request_handler(ClassConfirmationIntentHandler())
sb.add_request_handler(CalendarIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
