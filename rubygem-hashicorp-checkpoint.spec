%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from hashicorp-checkpoint-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hashicorp-checkpoint

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: Internal HashiCorp service to check version information
Group: Development/Languages
License: MPLv2.0
URL: http://www.hashicorp.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
# BuildRequires: %{?scl_prefix}rubygem(rspec) => 3.0.0
# BuildRequires: %{?scl_prefix}rubygem(rspec) < 3.1
# BuildRequires: %{?scl_prefix}rubygem(rspec-its) => 1.0.0
# BuildRequires: %{?scl_prefix}rubygem(rspec-its) < 1.1
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Internal HashiCorp service to check version information.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# We need RSpec3
# Run the test suite
#%%check
#pushd .%%{gem_instdir}
#rspec spec
#popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/ruby-checkpoint.gemspec
%exclude %{gem_instdir}/.gitignore
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/spec

%changelog
* Tue Sep 09 2014 Josef Stribny <jstribny@redhat.com> - 0.1.4-1
- Initial package
