# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


###############################################################################
###############################################################################
###############################################################################


import pytest


from innvestigate.utils.tests import dryrun

from innvestigate.analyzer import BaselineGradient
from innvestigate.analyzer import Gradient

from innvestigate.analyzer import Deconvnet
from innvestigate.analyzer import GuidedBackprop

from innvestigate.analyzer import IntegratedGradients

from innvestigate.analyzer import SmoothGrad


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__BaselineGradient():

    def method(model):
        return BaselineGradient(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__BaselineGradient():

    def method(model):
        return BaselineGradient(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__BaselineGradient():

    def method(model):
        return BaselineGradient(model)

    dryrun.test_analyzer(method, "imagenet.*")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__Gradient():

    def method(model):
        return Gradient(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__Gradient():

    def method(model):
        return Gradient(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__Gradient():

    def method(model):
        return Gradient(model)

    dryrun.test_analyzer(method, "imagenet.*")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__Deconvnet():

    def method(model):
        return Deconvnet(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__Deconvnet():

    def method(model):
        return Deconvnet(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__Deconvnet():

    def method(model):
        return Deconvnet(model)

    dryrun.test_analyzer(method, "imagenet.*")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__GuidedBackprop():

    def method(model):
        return GuidedBackprop(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__GuidedBackprop():

    def method(model):
        return GuidedBackprop(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__GuidedBackprop():

    def method(model):
        return GuidedBackprop(model)

    dryrun.test_analyzer(method, "imagenet.*")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__IntegratedGradients():

    def method(model):
        return IntegratedGradients(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__IntegratedGradients():

    def method(model):
        return IntegratedGradients(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__IntegratedGradients():

    def method(model):
        return IntegratedGradients(model, steps=2)

    dryrun.test_analyzer(method, "imagenet.*")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__SmoothGrad():

    def method(model):
        return SmoothGrad(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__SmoothGrad():

    def method(model):
        return SmoothGrad(model)

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.slow
@pytest.mark.application
@pytest.mark.imagenet
def test_imagenet__SmoothGrad():

    def method(model):
        return SmoothGrad(model, augment_by_n=2)

    dryrun.test_analyzer(method, "imagenet.*")