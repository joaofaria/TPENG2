from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Grupo')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "group"]

    def __init__(self, *args, **kwargs):
        super(UsuarioCreationForm, self).__init__(*args, **kwargs)
        self.fields['group'].label_from_instance = lambda obj: obj.name

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()  # Salve o usuário primeiro

        group_id = self.cleaned_data.get('group').id

        if group_id:
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            user.save()  # Salve novamente após adicionar o grupo

        return user

class UsuarioChangeForm(UserChangeForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Grupo')

    class Meta:
        model = User
        fields = ["username", "group"]  # Remova "password1" e "password2" desta lista

    def __init__(self, *args, **kwargs):
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)
        self.fields['group'].label_from_instance = lambda obj: obj.name

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()  # Salve o usuário primeiro

        group_id = self.cleaned_data.get('group').id

        if group_id:
            group = Group.objects.get(id=group_id)
            user.groups.set([group])  # Substitua os grupos existentes pelo novo grupo
            user.save()  # Salve novamente após adicionar o grupo

        return user


class GroupCreationForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Permissões'
    )

    class Meta:
        model = Group
        fields = ['name']

    def save(self, commit=True):
        group = super().save(commit=False)

        if commit:
            group.save()

        group.permissions.set(self.cleaned_data['permissions'])

        return group
